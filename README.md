# eh2ch
Convert Everhood battles to Clone Hero charts

# Warning
This script does best effort conversion and some elements may be lost

# How to use
1. Download [AssetStudio](https://github.com/aelurum/AssetStudio)
2. Open Everhood_Data folder in AssetStudio
3. Go to Asset List
4. Type "Chart" in the filter and sort by size
5. Click on any entry with the EXACT name "Chart"
6. If it asks you to select the assembly folder, use Everhood_Data\Managed
7. Pick the chart you want, right click it and click "Export selected assets"
8. After you got the JSON file, you need to run eh2ch: `python eh2ch.py [path to .json]`
9. notes.chart should appear in the current directory, you can edit it and export with Moonscraper

# Extracting song.wav
Just filter assets by AudioClip type and find the song
