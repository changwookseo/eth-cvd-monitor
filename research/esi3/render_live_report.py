"""Render the verified Binance USD-M subsection of the ESI 3.0 research report."""
import json
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

DATA = Path(__file__).resolve().parent / "data"
KST = ZoneInfo("Asia/Seoul")


def kst(epoch_ms):
    return datetime.fromtimestamp(epoch_ms / 1000, KST).strftime("%Y-%m-%d %H:%M:%S")


def render(snapshot):
    oi = snapshot["open_interest"]
    funding = snapshot["funding"]
    cvd = snapshot["futures_cvd_5m"]
    buy = Decimal(cvd["taker_buy_eth"])
    sell = Decimal(cvd["taker_sell_eth"])
    net = Decimal(cvd["net_eth"])
    if buy - sell != net:
        raise ValueError("Futures CVD does not match taker volumes")
    rate_percent = Decimal(funding["rate"]) * 100
    return "\n".join([
        "# ETH ESI 3.0 연구 보고서 | Binance 선물 수급",
        "",
        f"수집 기준 {kst(snapshot['collected_epoch_ms'])} KST",
        "",
        f"{snapshot['exchange']} / {snapshot['symbol']}",
        "",
        "| 지표 | 값 | 관측 시각 또는 구간 (KST) |",
        "|---|---:|---|",
        f"| 미결제약정 | {Decimal(oi['eth']):,.3f} ETH | {kst(oi['epoch_ms'])} |",
        f"| 최근 확정 펀딩비 | {rate_percent:+.6f}% | {kst(funding['epoch_ms'])} |",
        f"| 5분 선물 매수 체결량 | {buy:,.3f} ETH | {kst(cvd['open_epoch_ms'])} ~ {kst(cvd['end_exclusive_epoch_ms'])} |",
        f"| 5분 선물 매도 체결량 | {sell:,.3f} ETH | 같은 구간 |",
        f"| 5분 선물 순 CVD | {net:+,.3f} ETH | 같은 구간 |",
        "",
        "[원본 스냅샷](binance_live_latest.json)",
        "",
    ])


if __name__ == "__main__":
    snapshot = json.loads((DATA / "binance_live_latest.json").read_text(encoding="utf-8"))
    (DATA / "binance_live_report.md").write_text(render(snapshot), encoding="utf-8")
