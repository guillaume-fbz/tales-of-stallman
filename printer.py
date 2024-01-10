class Printer:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.spooler = []

    def print(self):
        if not self.spooler:
            print("Spooler is empty. Nothing to print.")
            return

        print(f"Printing documents with {self.brand} {self.model}:")
        for document in self.spooler:
            print(f"Printing: {document} ... OK")

        print("All documents have been printed.")
        self.spooler = []

    def add_to_spooler(self, document):
        self.spooler.append(document)
        print(f"{document} has been added to spooler.")


printer = Printer(brand="XEROX", model="9700")

printer.add_to_spooler("oak.txt")
printer.add_to_spooler("pokedex.pdf")
printer.add_to_spooler("m1cr0s0ft.docx")

printer.print()
