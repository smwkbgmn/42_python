from give_bmi import give_bmi, apply_limit


def main() -> None:
    # h = [2.71, 1.15]
    # h = [2.71, -1.15]
    # h = [2.71, 0]
    # h = [2.71, "True"]
    h = [2.71, True]
    # h = [2.71, 1.15, 5]
    # h = {2.71, 1.15}
    w = [165.3, 38.4]

    bmi = give_bmi(h, w)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()


