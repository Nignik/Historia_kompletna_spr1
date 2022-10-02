class Task:
    def __init__(self, question, answer):
        self.answer = answer
        self.question = question


izabela_jagiellonka_life = Task("W jakich latach zyla Izabela Jagiellonka?\n",
                                "1519-1559\n")
izabela_jagiellonka_events = Task("Co osiagnela Izabela Jagiellonka?\n",
                                  "Zostala wladca wegier, wziela Siemogrod przy podziale Wegier\n")

wladyslaw_II_jagielonczyk_life = Task("W jakich latach zyl wladyslaw II jagiellonczyk\n",
                                      "1456-1516\n")

izabela_jagiellonka_list = [izabela_jagiellonka_life, izabela_jagiellonka_events]
wladyslaw_II_jagielonczyk_list = [wladyslaw_II_jagielonczyk_life]

questions_map = {
    "Izabela Jagiellonka": izabela_jagiellonka_list,
    "Wladyslaw II Jagiellonczyk": wladyslaw_II_jagielonczyk_list
}
