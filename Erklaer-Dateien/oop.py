# Da es diesbezüglich in der Übung noch Schwierigkeiten gab, stelle ich hier noch mal das Konzept der
# objektorientierten Programmierung (OOP) vor.

# Ich werde dies anhand einer Beispiel-Klasse simulieren, die ein Bankkonto darstellt.
# Zuerst nutzt man das "class"-Schlüsselwort, um eine Klasse zu definieren.


class BankAccount:

    # Notiz: Man schreibt Klassennamen groß und statt _ schreibt man Buchstaben im Klassennamen groß, wenn ein
    # neues Wort beginnt (per Konvention).

    # Das Erste, was ich tun will, wenn ich eine Klasse erstelle, ist eine init-Methode zu schreiben.
    # Wenn man ein Objekt der Klasse erzeugt, wird die init aufgerufen. Z.B. list(), set() etc.
    # In die Klammer kommen die Argumente für die init, die dann ausgeführt.

    def __init__(self, account_balance: int, transfer_limit: int) -> None:
        # die init hat immer zwingend "self" als erstes Argument. Das ist eine Referenz auf - well - sich selbst.
        # Das soll heißen, ich kann self nutzen, um dem Objekt, das ich erzeuge Attribute und Methoden zuzuweisen.

        # Darüber hinaus kann man noch mehr Argumente angeben, die dann beim Erstellen eines Objekts der Klasse angegeben
        # müssen.

        # Attribute sind sozusagen Variable (mit self. davor) und Methoden sind im Wesentlichen Funktionen, die
        # speziell für diese Klasse gedacht sind. Z.B. gibt es eine sort()-Methode für Listen. Der Hauptunterschied ist,
        # dass Methoden über die Punkt-Syntax aufgerufen werden (z.B. x.sort(), falls x eine Liste ist, nicht sort(x).
        # Alle Attribute einer Klasse sollten in der init deklariert werden.

        self._account_balance = account_balance
        self._transfer_limit = transfer_limit
        self._transferred_today = 0

    # Auf mein Bankkonto will ich jetzt Geld einzahlen können. Dafür schreibe ich eine Methode.
    # Wenn ich innerhalb einer Methode auf Attribute oder Methoden dieser Klasse (z.B. account_balance) zugreifen
    # will, muss self das erste Argument der Methode sein. Für den Anfang schadet es nicht, es einfach immer hinzuschreiben.

    def deposit_money(self, amount: int) -> None:
        self._account_balance += amount

    # Analog will ich auch Geld abheben können.

    def withdraw_money(self, amount: int) -> None:
        # Check, ob ich genug Geld habe.
        if self._account_balance - amount >= 0:
            self._account_balance -= amount
        else:
            # Fehler werfen wäre besser, aber das ist wahrscheinlich anschaulicher.
            print(f"Ihr Kontostand ({self._account_balance}€) ist zu niedrig, um {amount}€ abheben zu können.")

    # Jetzt wäre es noch gut, Geld überweisen zu können. Dafür muss man hier etwas Vorarbeit leisten.

    # Hilfsfunktion, um zu checken, ob eine Transaktion erlaubt ist.

    def is_transaction_valid(self, amount: int) -> bool:
        return self._transferred_today + amount <= self._transfer_limit

    # Analog zum Anpassen des transferierten Betrags

    def update_transferred_today(self, amount: int) -> None:
        self._transferred_today += amount

    # Ich will also endlich von meinem Konto auf ein anderes Konto überweisen können.

    def transfer_money_to(self, other: "BankAccount", amount: int) -> None:
        # Checke, ob ich genug Geld habe.

        if self._account_balance - amount >= 0:
            # Checke, ob ich oder die andere Person nach der Transaktion das Überweisungslimit nicht verletzt haben.

            # Wenn man Methoden aufruft, verwendet man die "Punkt"-Syntax. Also erst den Namen der Variable bzw self,
            # falls es sich auf diese Klasse bezieht und dann einen Punkt und den Funktionsaufruf. Auch wenn self als
            # erstes Argument der Methoden gelistet wird, wird es nicht in den Klammern übergeben, sondern es ist das,
            # was vor dem Punkt steht. In der Praxis sieht das dann so aus:

            if self.is_transaction_valid(amount) and other.is_transaction_valid(amount):
                self.withdraw_money(amount)
                other.deposit_money(amount)

                self.update_transferred_today(amount)
                other.update_transferred_today(amount)

            else:
                # Fehler werfen wäre besser, aber das ist wahrscheinlich anschaulicher.
                print("Die Transaktion überschreitet das Transaktionslimit für einen Tag. Probieren Sie es mit einem geringeren Betrag oder morgen erneut.")

        else:
            print(f"Ihr Kontostand ({self._account_balance}€) ist zu niedrig, um {amount}€ überweisen zu können.")

    # Abschliessend würde ich Objekte der Klasse gescheit printen können und nicht erfahren, dass es Objekte der
    # Klasse BankAccount sind, die an Speicherplatz xy sind.
    # Dafür muss die __str__-Methode überladen werden

    def __str__(self) -> str:
        return f"BankAccount(Kontostand: {self._account_balance}, Transaktionslimit: {self._transfer_limit}, heute transferiert: {self._transferred_today})"


# Jetzt schauen wir uns mal an, wie das dann am Ende aussieht.
# Wie gesagt, ist es eine gute Praxis, seinen Code, der ausgeführt wird, in eine main-Funktion zu schreiben.


def main():
    my_bank_account = BankAccount(0, 1000)
    other_bank_account = BankAccount(500, 1500)
    print(my_bank_account)
    print(other_bank_account)
    print()

    # Zahlen wir etwas Geld auf meinem Konto ein und heben welches auf dem anderen ab.

    my_bank_account.deposit_money(100)
    other_bank_account.withdraw_money(100)

    print(my_bank_account)
    print(other_bank_account)
    print()

    # Jetzt überweise ich etwas auf das andere Konto

    my_bank_account.transfer_money_to(other_bank_account, 200)
    # Oh, so viel Geld habe ich nicht. Das gab eine Fehlermeldung!

    # Dann muss ich zuerst Geld einzahlen.

    my_bank_account.deposit_money(1000)

    print()
    print(my_bank_account)
    print(other_bank_account)
    print()

    # Jetzt will ich aber alles überweisen!

    my_bank_account.transfer_money_to(other_bank_account, 1100)
    # Mist, das überschreitet mein Transaktionslimit

    # Dann eben weniger!

    my_bank_account.transfer_money_to(other_bank_account, 200)

    print()
    print(my_bank_account)
    print(other_bank_account)


# Hier startet das Programm dann tatsächlich, wie in der Übung gezeigt:

if __name__ == '__main__':
    main()
