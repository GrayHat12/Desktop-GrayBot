import GrayPlot
import webbrowser

inp = input('Location : ')
gmap = GrayPlot.GoogleMapPlotter.from_geocode(inp)
gmap.draw("googMap.html")
webbrowser.open_new('googMap.html')