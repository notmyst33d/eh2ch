import os
import sys
import json
import math
from dataclasses import dataclass

path = os.path.dirname(os.path.realpath(__file__))

@dataclass
class Note:
    tick: int
    color: int
    type: str

    @staticmethod
    def from_dict(data):
        assert len(data.keys()) == 6
        # No idea what these ID's mean
        # assert data["noteID"] == 0
        assert data["noteCorridorID"] == data["noteColorID"]
        # What does this do?
        # assert data["noteDurationTick"] == 0.0
        assert math.ceil(data["noteTick"]) == data["noteTick"]

        return Note(
            int(data["noteTick"]),
            data["noteColorID"],
            data["noteTypeID"]
        )

    @staticmethod
    def from_array(data):
        return [Note.from_dict(entry) for entry in data]

    def to_ch(self):
        return f"  {self.tick} = {self.type} {self.color} 0"

@dataclass
class Section:
    name: int
    tick: int

    @staticmethod
    def from_dict(data):
        return Section(
            data["sectionID"],
            int(data["sectionTick"])
        )

    @staticmethod
    def from_array(data):
        return [Section.from_dict(entry) for entry in data]

    def to_ch(self):
        return f"  {self.tick} = E \"section {self.name}\""

@dataclass
class Chart:
    name: str
    resolution: int
    bpm: int
    sections: list[Section]
    notes: list[Note]

    @staticmethod
    def from_dict(data):
        return Chart(
            data["songName"],
            data["resolution"],
            data["bpm"],
            Section.from_array(data["sections"]),
            Note.from_array(data["notes"]),
        )

with open(sys.argv[1], "r") as file:
    chart = json.load(file)

with open(f"{path}/template.chart", "r") as file:
    template = file.read()

chart = Chart.from_dict(chart)
notes = "\n".join([note.to_ch() for note in chart.notes])
sections = "\n".join([section.to_ch() for section in chart.sections])

template = template.replace("%NAME%", chart.name)
template = template.replace("%RESOLUTION%", str(chart.resolution))
template = template.replace("%BPM%", str(chart.bpm))
template = template.replace("%NOTES%", notes)
template = template.replace("%SECTIONS%", sections)

with open("notes.chart", "w") as file:
    file.write(template)
