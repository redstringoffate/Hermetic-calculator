from utils import normalize

def hermetic_lot(asc, a, b, sect):
    if sect == "Day":
        return normalize(asc + a - b)
    else:
        return normalize(asc + b - a)

def calculate_all_lots(positions, sect):
    asc = positions["Asc"]
    results = {}

    # Base
    results["Fortune"] = hermetic_lot(
        asc, positions["Moon"], positions["Sun"], sect
    )
    results["Spirit"] = hermetic_lot(
        asc, positions["Sun"], positions["Moon"], sect
    )

    # Derived (corrected)
    results["Eros"] = hermetic_lot(
        asc, positions["Venus"], results["Spirit"], sect
    )
    results["Courage"] = hermetic_lot(
        asc, positions["Mars"], results["Fortune"], sect
    )
    results["Victory"] = hermetic_lot(
        asc, positions["Jupiter"], results["Spirit"], sect
    )
    results["Necessity"] = hermetic_lot(
        asc, results["Fortune"], positions["Mercury"], sect
    )
    results["Nemesis"] = hermetic_lot(
        asc, results["Spirit"], positions["Saturn"], sect
    )

    return results


