import altair as alt

def theme_desarroio():
    font = "Sanchez"
    labelFont = "Sanchez"
    sourceFont = "Sanchez"
    axisColor = "#000000"
    gridColor = "#DEDDDD"
    textColor = "#808080"
    markColor = "#5297AC" # azul oficial
    backgroundColor = "#F9F7F3" # 100%
    main_palette = ["#5297AC", # Cluster 1 azul
                    "#ac6e69", # Cluster 2 coral/marrón
                    "#4ba479", # Cluster 3 verde
                    "#e2a920", 
                    "#BAA6A5", 
                    "#A6C6C1", 
                    "#55b748", 
                    "#5c5859", 
                    "#db2b27", 
                   ]
    sequential_palette = ["#cfe8f3", 
                          "#a2d4ec", 
                          "#73bfe2", 
                          "#46abdb", 
                          "#1696d2", 
                          "#12719e", 
                         ]
    
    return {
        "width": 685, # from the guide
        "height": 380, # not in the guide
        "config" : {
             "title": {'font': font, 
                       'fontSize': 18,
                       'fontWeight': 600,
                       'fontColor' : "#000000",
                       'offset': 24, # espacio hacia abajo?
                       'anchor':'start'
                       },
             "axisX": {
                  "labelFont": font,
                  "titleFont": font,
                  "domainColor": axisColor,
                  "grid": False,
                  "domain": True
             },
             "axisY": {
                  "labelFont": font,
                  "titleFont": font,
                  "domainColor": axisColor,
                  "domain": True
             },
             "header": {
                  "labelFont": font,
                  "titleFont": font
             },
              "range": {
                  "category": main_palette,
                  "diverging": sequential_palette
             },
             "view": {
                  "stroke": "transparent",
             },
             "legend": {
                  "labelFont": font,
                  "titleFont": font,
                  "symbolType": 'circle',
                  "padding": 1
                  },
                        ### MARKS CONFIGURATIONS ###
            "area": {
               "fill": markColor,
           },
           "line": {
               "color": markColor,
               "stroke": markColor,
               "strokeWidth": 4,
           },
           "trail": {
               "color": "#ff0800", #no sé qué es
               "stroke": "#ff0800", #no sé qué es
               "strokeWidth": 100, #no sé qué es
               "size": 50, #no sé qué es
           },
           "path": {
               "stroke": "#ff0800", # no sé que es
               "strokeWidth": 0.1, # no sé que es
           },
           "point": {
               "filled": True,
               "opacity": 1, # 0.7 default,
               "size": 100, # 30 default,
           },
           "circle": {
               "filled": True,
               "opacity": 1, # 0.7 default,
               "size": 100, # 30 default,
               "color": markColor,
           },
           "text": {
               "font": sourceFont,
               "color": textColor,
               "fontSize": 11,
               "align": "right",
               "fontWeight": 400,
               "size": 11,
           }, 
           "bar": {
                "binSpacing": 1,
                "continuousBandSize": 30,
                "discreteBandSize": 30,
                "fill": markColor,
                "stroke": False,
            },
             'background': backgroundColor             
        }
    }

alt.themes.register('theme_desarroio', theme_desarroio)
alt.themes.enable('theme_desarroio')