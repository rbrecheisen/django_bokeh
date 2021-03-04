from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components


def home(request):

    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]

    plot = figure(
        title='Line graph',
        x_axis_label='X',
        y_axis_label='Y',
        plot_width=400,
        plot_height=400,
    )

    plot.line(x, y, line_width=2)

    script, div = components(plot)
    return render(request, 'base.html', {'script': script, 'div': div})
