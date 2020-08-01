import json

if __name__ == "__main__":

    X = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    Operator = ["*", "/", "+", "-"]
    result = {}
    for a in X:
        for b in X:
            for c in X:
                for d in X:
                    for c1 in Operator:
                        for c2 in Operator:
                            for c3 in Operator:
                                sum = eval(
                                    "(({a}{c1}{b}){c2}{c}){c3}{d}".format(
                                        a=a, b=b, c=c, d=d, c1=c1, c2=c2, c3=c3
                                    )
                                )
                                if sum == 24:
                                    # print(
                                    #     a.rjust(2, "0")
                                    #     + b.rjust(2, "0")
                                    #     + c.rjust(2, "0")
                                    #     + d.rjust(2, "0")
                                    #     + "的解法"
                                    #     + "(({a}{c1}{b}){c2}{c}){c3}{d}".format(
                                    #         a=a, b=b, c=c, d=d, c1=c1, c2=c2, c3=c3
                                    #     )
                                    # )
                                    key_str = ",".join(
                                        sorted(
                                            [
                                                a.rjust(2, "0"),
                                                b.rjust(2, "0"),
                                                c.rjust(2, "0"),
                                                d.rjust(2, "0"),
                                            ]
                                        )
                                    )
                                    # print(key_str)
                                    if result.get(key_str, None) is None:
                                        result[key_str] = [
                                            "(({a}{c1}{b}){c2}{c}){c3}{d}".format(
                                                a=a, b=b, c=c, d=d, c1=c1, c2=c2, c3=c3
                                            )
                                        ]
                                    else:
                                        result[key_str].append(
                                            "(({a}{c1}{b}){c2}{c}){c3}{d}".format(
                                                a=a, b=b, c=c, d=d, c1=c1, c2=c2, c3=c3
                                            )
                                        )
    print(result)
    json.dump(result, open("result.json", "w+"))
