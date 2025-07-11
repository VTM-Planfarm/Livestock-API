from functions.vars import stock_classes, seasons

def create_json_data(seasonal_sheep: list, group: int = 1, **kwargs) -> dict:
    json_data = agro_zone(kwargs["northOfTropicOfCapricorn"], kwargs["rainfallAbove600mm"])

    # Create stock class data structure
    json_data["sheep"] = [
        {
            "classes": {}
        }
    ] * group

    for i in range(group):
        for stock_class in stock_classes:
            json_data["sheep"][i]["classes"][stock_class] = {}
            for season in seasons:
                sheep_data = seasonal_sheep[i][stock_class][season]

                json_data = seasonal_data(
                    json_data,
                    stock_class,
                    season,
                    **sheep_data,
                    index=i
                )

    return json_data

def agro_zone(northOfTropicOfCapricorn=False, rainfallAbove600mm=False) -> dict:
    return {
        "state": "wa_sw",
        "northOfTropicOfCapricorn": northOfTropicOfCapricorn,
        "rainfallAbove600mm": rainfallAbove600mm
    }

def seasonal_data(
        json_data: dict,
        stock_class: str,
        season: str,
        head: int,
        liveweight: float,
        liveweightGain: float,
        crudeProtein: float = 0,
        dryMatterDigestibility: float = 0,
        feedAvailability: float = 0,
        index: int = 0
) -> dict:
    json_data["sheep"][index]["classes"][stock_class][season] = {
        "head": head,
        "liveweight": liveweight,
        "liveweightGain": liveweightGain,
        "crudeProtein": crudeProtein,
        "dryMatterDigestibility": dryMatterDigestibility,
        "feedAvailability": feedAvailability
    }

    return json_data