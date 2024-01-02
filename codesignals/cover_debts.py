def solution(s, debts, interests):

    month_spend = []
    def check_max_interest(interests):
        """return index of highest interest"""
        index_ = max(interests)

        return (index_, interests.index(index_))

    def pay_loan(debts):
        min_spend = 0.1 * s
        for index, debt in enumerate(debts):
            if debt == 0:
                continue
            remainder = 0

            if debt < min_spend:
                debts[index] = 0
                month_spend.append(debt)
                min_spend -= debt
            debts[index] = debt - min_spend
            month_spend.append(debt)

        return debts

    def apply_interest(debts, interests):

        for i, debt in enumerate(debts):
            if debt > 0:
                debts[i] += (debt * (interests[i] / 100))

        return debts

    while not all(debts):
        pay_loan(debts)
        apply_interest(debts)


    return sum(month_spend) 
