from Are_Rhymes import are_rhyming
import utils
import matplotlib.pyplot as plt
import numpy as np

results = [ False, True, False, False, True, False, False, True, False, False, True, True, False ]
index = -1

class RhymeGroup:
    def __init__(self, first_line_number, lines, rhyming_data, group_name):
        self.first_line_number = first_line_number
        self.lines = lines
        self.rhyming_data = rhyming_data
        self.group_name = group_name

    def __str__(self):
        result = self.group_name
        result += "\n-----------"
        for line in self.lines:
            result += ("\n" + line)

        return result


class RhymeGrouper:

    def init_rhyme_lists(self):
        self.rhyme_groups = { "even": [], "cross": [], "surrounding": [], "unspecified": []}
        self.rhyme_groups_unprocessed = { "even": [], "cross": [], "surrounding": [], "unspecified": [] }
        self.rhyme_list = []
        self.rhyme_list_unprocessed = []

    def __init__(self, rhyming_determinant):
        self.rhyming_determinant = rhyming_determinant
        self.lines_buffer = [ None, None, None, None ] # 4 linie bufora
        self.current_line_number = -1
        self.rhyme_groups = None
        self.rhyme_groups_unprocessed = None
        self.rhyme_list = None
        self.rhyme_list_unprocessed = None
        self.file = None

    def read_to_buffer(self, offset): # offset = 1-4, liczba następnych linii do sczytania
        # Dopasowania wskaźnika pierwszej linii
        if self.current_line_number == -1:
            self.current_line_number = 0
        else:
            self.current_line_number += offset
        
        # Przesuwanie bufora
        for i in range(4 - offset):
            self.lines_buffer[i] = self.lines_buffer[i + offset]
         
        # Doczytywanie do bufora
        lines_read = 0
        while lines_read < offset:
            line = self.file.readline()

            # Koniec pliku źródłowego
            if line == '':
                self.lines_buffer[lines_read + 4 - offset] = None
                lines_read += 1

            else:
                # Sprawdź, czy linia ma w ogóle zawartość
                stripped_no_punctuation = utils.strip_punctuation(line).strip().replace("\n", "").replace("\r", "")
                stripped = line.strip().replace("\n", "").replace("\r", "") # na początku pozbywamy się whitespaców
                if(stripped_no_punctuation != ""):
                    # wykonujemy to tylko, jeśli string nie jest pusty
                    self.lines_buffer[lines_read + 4 - offset] = stripped
                    lines_read += 1


    def buffer_valid_for_grouping(self):
        for i in range(4):
            if self.lines_buffer[i] is None:
                return False
        
        return True

    def group_buffer(self):
        rhymes_with = [[], [], [], []]
        lines = self.lines_buffer.copy()

        for i in range(4):
            for j in range(3-i):
                # Sprawdzenie rymowania
                if self.rhyming_determinant(lines[i], lines[1 + i + j]):
                    rhymes_with[i].append(1 + i + j)
                    rhymes_with[1 + i + j].append(i)

        for i in range(4):
            # Warunek brakującego rymu (brak zasady dot. rymowania się tego zestawu linii)
            if rhymes_with[i].__len__() == 0:
                return RhymeGroup(self.current_line_number, lines, rhymes_with, "unspecified")

            # Warunek jednoznacznego rymu
            if rhymes_with[i].__len__() == 1:
                lines_ids = [0, 1, 2, 3]
                lines_ids.remove(i)
                lines_ids.remove(rhymes_with[i][0])

                if rhymes_with[lines_ids[0]].__contains__(lines_ids[1]):
                    if lines_ids[1] - lines_ids[0] == abs(i - rhymes_with[i][0]):
                        if lines_ids[1] - lines_ids[0] == 1:
                            group_name = "even"
                        else:
                            group_name = "cross"
                    else:
                        group_name = "surrounding"
        
                else:
                    group_name = "unspecified"

                return RhymeGroup(self.current_line_number, lines, rhymes_with, group_name)

        # No valid pattern detected
        return RhymeGroup(self.current_line_number, lines, rhymes_with, "unspecified")

    def process_lists(self):
        lines_buffer = []
        unspecified_line_number = None

        for rhyme in self.rhyme_list_unprocessed:
            if rhyme.group_name == "unspecified":
                if unspecified_line_number is None:
                    unspecified_line_number = rhyme.first_line_number

                # Przypadek ostatnich linii pliku
                if rhyme.rhyming_data == None:
                    for i in range(4):
                        if not rhyme.lines[i] is None:
                            lines_buffer.append(rhyme.lines[i])

                else:
                    lines_buffer.append(rhyme.lines[0])

            else:
                # Zapisywanie danych o niezrymowanych liniach
                if lines_buffer.__len__() > 0:
                    current_rhyme = RhymeGroup(unspecified_line_number, lines_buffer.copy(), None, "unspecified")
                    self.rhyme_list.append(current_rhyme)
                    self.rhyme_groups["unspecified"].append(current_rhyme)

                    lines_buffer.clear()
                    unspecified_line_number = None

                # Zapisywanie danych o zrymowanych liniach
                self.rhyme_list.append(rhyme)
                self.rhyme_groups[rhyme.group_name].append(rhyme)

        if not unspecified_line_number is None:
            current_rhyme = RhymeGroup(unspecified_line_number, lines_buffer.copy(), None, "unspecified")
            self.rhyme_list.append(current_rhyme)
            self.rhyme_groups["unspecified"].append(current_rhyme)
           

    def group(self, source_file):
        self.init_rhyme_lists()
        self.file = open(source_file, mode="r", encoding="utf-8")

        self.read_to_buffer(4)
        while(self.buffer_valid_for_grouping()):
            rhyme = self.group_buffer()
            self.rhyme_list_unprocessed.append(rhyme)
            self.rhyme_groups_unprocessed[rhyme.group_name].append(rhyme)

            if rhyme.group_name == "unspecified":
                self.read_to_buffer(1)
            else:
                self.read_to_buffer(4)

        if not self.lines_buffer[0] is None:
            rhyme = RhymeGroup(self.current_line_number, self.lines_buffer.copy(), None, "unspecified")
            self.rhyme_groups_unprocessed["unspecified"].append(rhyme)
            self.rhyme_list_unprocessed.append(rhyme)

        self.process_lists()

        self.file.close()
        self.file = None

def random_determinant(line1, line2):
    global index
    global results
    index += 1
    if index < results.__len__():
        return results[index]
    else:
        return False