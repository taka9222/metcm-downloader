from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RangeLocation:
    code: str
    name: str
    category: str  # domestic / overseas
    country: str
    region: str  # 国内: 都道府県、国外: 州・地域
    lat: float
    lon: float
    description: str = ""

    @property
    def location_name(self) -> str:
        """表示用所在地"""
        return f"{self.region}, {self.country}"

    def to_row(self) -> dict:
        return {
            "code": self.code,
            "loc": self.name,
            "region": self.region,
            "country": self.country,
            "lat": self.lat,
            "lon": self.lon,
        }


RANGES: list[RangeLocation] = [
    RangeLocation(
        code="Y",
        name="矢臼別演習場",
        category="domestic",
        country="日本",
        region="北海道",
        lat=43.2997,
        lon=144.9873,
    ),
    RangeLocation(
        code="K",
        name="上富良野演習場",
        category="domestic",
        country="日本",
        region="北海道",
        lat=43.4230,
        lon=142.4800,
    ),
    RangeLocation(
        code="I",
        name="岩手山演習場",
        category="domestic",
        country="日本",
        region="岩手県",
        lat=39.8650,
        lon=140.9730,
    ),
    RangeLocation(
        code="O",
        name="王城寺原演習場",
        category="domestic",
        country="日本",
        region="宮城県",
        lat=38.5710,
        lon=140.8610,
    ),
    RangeLocation(
        code="E",
        name="東富士演習場",
        category="domestic",
        country="日本",
        region="静岡県",
        lat=35.2947,
        lon=138.8536,
    ),
    RangeLocation(
        code="N",
        name="北富士演習場",
        category="domestic",
        country="日本",
        region="山梨県",
        lat=35.4500,
        lon=138.8000,
    ),
    RangeLocation(
        code="A",
        name="饗庭野演習場",
        category="domestic",
        country="日本",
        region="滋賀県",
        lat=35.3460,
        lon=136.0390,
    ),
    RangeLocation(
        code="H",
        name="日出生台演習場",
        category="domestic",
        country="日本",
        region="大分県",
        lat=33.2860,
        lon=131.3990,
    ),
    RangeLocation(
        code="S",
        name="防衛装備庁下北試験場",
        category="domestic",
        country="日本",
        region="青森県",
        lat=41.3050,
        lon=141.3070,
    ),
    RangeLocation(
        code="YPG",
        name="Yuma Proving Ground",
        category="overseas",
        country="USA",
        region="Arizona",
        lat=32.8600,
        lon=-114.4000,
    ),
]


def get_ranges(category: str) -> list[RangeLocation]:
    return [r for r in RANGES if r.category == category]

DOMESTIC_RANGES = get_ranges("domestic")
OVERSEAS_RANGES = get_ranges("overseas")