def get_partial_match(dict1, dict2) -> list[str]:
    """
    Возврат списка с совпадающими ключами в обоих переданных словарях
    """
    matches = []

    for key1 in dict1.keys():
        for key2 in dict2.keys():
            if key1 in key2 or key2 in key1:
                matches.append((key1, key2))

    return matches
