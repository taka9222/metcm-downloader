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
        lat=43.288505,
        lon=144.771992,
    ),
    RangeLocation(
        code="K",
        name="上富良野演習場",
        category="domestic",
        country="日本",
        region="北海道",
        lat=43.420159,
        lon=142.575858,
    ),
    RangeLocation(
        code="I",
        name="岩手山演習場",
        category="domestic",
        country="日本",
        region="岩手県",
        lat=39.853671,
        lon=141.056602,
    ),
    RangeLocation(
        code="O",
        name="王城寺原演習場",
        category="domestic",
        country="日本",
        region="宮城県",
        lat=38.491719,
        lon=140.734131,
    ),
    RangeLocation(
        code="E",
        name="東富士演習場",
        category="domestic",
        country="日本",
        region="静岡県",
        lat=35.297165,
        lon=138.824322,
    ),
    RangeLocation(
        code="N",
        name="北富士演習場",
        category="domestic",
        country="日本",
        region="山梨県",
        lat=35.399786,
        lon=138.818203,
    ),
    RangeLocation(
        code="A",
        name="饗庭野演習場",
        category="domestic",
        country="日本",
        region="滋賀県",
        lat=35.387818,
        lon=135.964849,
    ),
    RangeLocation(
        code="H",
        name="日出生台演習場",
        category="domestic",
        country="日本",
        region="大分県",
        lat=33.307710,
        lon=131.257124,
    ),
    RangeLocation(
        code="S",
        name="防衛装備庁下北試験場",
        category="domestic",
        country="日本",
        region="青森県",
        lat=41.240080,
        lon=141.393885,
    ),
    RangeLocation(
        code="YPG-K",
        name="Yuma Proving Ground - KOFA Range",
        category="overseas",
        country="USA",
        region="Arizona",
        lat=32.914028,
        lon=-113.983390,
    ),
    RangeLocation(
        code="YPG-C",
        name="Yuma Proving Ground - Cibola Range",
        category="overseas",
        country="USA",
        region="Arizona",
        lat=33.333164,
        lon=-114.377756,
    ),
]


def get_ranges(category: str) -> list[RangeLocation]:
    return [r for r in RANGES if r.category == category]

DOMESTIC_RANGES = get_ranges("domestic")
OVERSEAS_RANGES = get_ranges("overseas")