import csv, io, zipfile, hashlib, json, os
from datetime import datetime, timezone, date, timedelta
from decimal import Decimal
from pathlib import Path
from urllib.request import urlopen, Request
from collections import defaultdict
BASE="https://assets.kraken.com/marketing/institutions/"
OUT=Path("research/esi3/data")
START=date(2020,1,1)
END=date(2026,10,1)
def main():
    audit={"status":"INCOMPLETE","source":BASE,"archive_end_exclusive":str(END),"errors":[]}
    OUT.mkdir(parents=True,exist_ok=True)
    try:
        # Treat the concatenated official split file as a seekable HTTP object.
        from bisect import bisect_right
        class Parts(io.RawIOBase):
            def __init__(self):
                self.urls=[BASE+f"Kraken_Trades_Full.zip.part{i:02}" for i in range(14)]
                self.offsets=[0]; self.pos=0
                for u in self.urls:
                    with urlopen(Request(u,method="HEAD"),timeout=60) as r:
                        self.offsets.append(self.offsets[-1]+int(r.headers["Content-Length"]))
            def seekable(self): return True
            def readable(self): return True
            def tell(self): return self.pos
            def seek(self,n,whence=0):
                self.pos=n if whence==0 else self.pos+n if whence==1 else self.offsets[-1]+n
                if self.pos<0: raise ValueError("negative seek")
                return self.pos
            def read(self,n=-1):
                n=min(n if n>=0 else self.offsets[-1],self.offsets[-1]-self.pos)
                chunks=[]
                while n>0:
                    i=bisect_right(self.offsets,self.pos)-1
                    a=self.pos-self.offsets[i]; k=min(n,self.offsets[i+1]-self.pos)
                    with urlopen(Request(self.urls[i],headers={"Range":f"bytes={a}-{a+k-1}"}),timeout=120) as r:
                        if r.status!=206: raise ValueError("Range unsupported")
                        v=r.read()
                        if len(v)!=k: raise ValueError("short read")
                    self.pos+=k;n-=k;chunks.append(v)
                return b"".join(chunks)
        rows=defaultdict(lambda:[Decimal(0),Decimal(0),0])
        prev=Decimal(-1); prev_id=None; digest=hashlib.sha256()
        with zipfile.ZipFile(Parts()) as z:
            names=[n for n in z.namelist() if Path(n).stem.upper() in ("ETHUSD","XETHZUSD")]
            if len(names)!=1: raise ValueError("ETH/USD member ambiguous: "+str(names))
            audit["member"]=names[0]; audit["member_crc32"]=z.getinfo(names[0]).CRC
            with z.open(names[0]) as f:
                def lines():
                    for line in f:
                        digest.update(line)
                        yield line.decode("utf-8-sig")
                for r in csv.DictReader(lines()):
                    t=Decimal(r["timestamp"]); v=Decimal(r["volume"]); p=Decimal(r["price"]); side=r["type"]; tid=int(r["trade_id"])
                    if not t.is_finite() or not v.is_finite() or not p.is_finite() or v<=0 or p<=0 or side not in ("b","s") or t<prev or (prev_id is not None and tid<=prev_id): raise ValueError("invalid or nonmonotonic trade")
                    prev=t;prev_id=tid
                    d=datetime.fromtimestamp(int(t),timezone.utc).date()
                    if START<=d<END:
                        row=rows[d];row[0 if side=="b" else 1]+=v;row[2]+=1
        audit["member_sha256"]=digest.hexdigest()
        audit["archive_integrity"]="ZIP member CRC verified on complete read; full split SHA256 not independently checked"
        audit["missing_dates"]=[str(START+timedelta(days=i)) for i in range((END-START).days) if START+timedelta(days=i) not in rows]
        dest=OUT/"kraken_spot_archive_daily.csv"
        with dest.open("w",newline="") as f:
            w=csv.writer(f);w.writerow(["date_utc","buy_eth","sell_eth","volume_eth","cvd_eth","trades"])
            for d,(b,s,n) in sorted(rows.items()):w.writerow([d,b,s,b+s,b-s,n])
        audit["rows"]=len(rows);audit["csv_sha256"]=hashlib.sha256(dest.read_bytes()).hexdigest()
        audit["status"]="ARCHIVE_PARTIAL_VALIDATED" if not audit["missing_dates"] else "INCOMPLETE"
    except Exception as e: audit["errors"].append(str(e))
    (OUT/"kraken_spot_archive_audit.json").write_text(json.dumps(audit,indent=2))
    return 0 if audit["status"]=="ARCHIVE_PARTIAL_VALIDATED" else 1
if __name__=="__main__": raise SystemExit(main())
