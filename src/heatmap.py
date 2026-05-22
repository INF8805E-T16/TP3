'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import hover_template

from template import THEME

def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    # the layout. Also don't forget to include the hover template.
    fig = px.imshow(
        data,
        labels=dict(x="Year", y="Neighborhood", color="Trees")
    )

    fig.update_layout(dragmode=False)

    fig.update_xaxes(
        tickvals=data.columns,
        ticktext=[str(col.year) for col in data.columns]
    )

    fig.update_traces(hovertemplate=hover_template.get_heatmap_hover_template())

    return fig
