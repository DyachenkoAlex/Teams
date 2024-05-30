from logic import *

teams = ["Milan", "Real", "Metalist"]
coaches = ["Rodrigo", "Antonio", "Mykola"]
same_nations = ["MykolaMetalist", "AntonioMilan","RodrigoReal"]

symbols = []

knowledge = And()

for coach in coaches:
    for team in teams:
        symbols.append(Symbol(f"{coach}{team}"))

for coach in coaches:
    knowledge.add(Or(
        Symbol(f"{coach}Milan"),
        Symbol(f"{coach}Real"),
        Symbol(f"{coach}Metalist"),
    ))

for coach in coaches:
    for t1 in teams:
        for t2 in teams:
            if t1 != t2:
                knowledge.add(
                    Implication(Symbol(f"{coach}{t1}"), Not(Symbol(f"{coach}{t2}")))
                )

for team in teams:
    for c1 in coaches:
        for c2 in coaches:
            if c1 != c2:
                knowledge.add(
                    Implication(Symbol(f"{c1}{team}"), Not(Symbol(f"{c2}{team}")))
                )

for same_nation in same_nations:
    knowledge.add(
        Not(Symbol(f"{same_nation}"))
    )

knowledge.add(
    Not(Symbol("AntonioMetalist"))
)

knowledge.add(
    Not(Symbol("MykolaReal"))
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
