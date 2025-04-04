import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    'fcc-forum-pageviews.csv',
    index_col='date',
    parse_dates=True
)

# Clean data - filter top and bottom 2.5% of data
df = df[
    (df['value'] > df['value'].quantile(0.025)) &
    (df['value'] < df['value'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    # Create a copy of our DataFrame
    df_line = df.copy()
    
    # Create figure in OOP style
    fig, ax = plt.subplots(figsize=(18, 6))
    
    # Plot data
    ax.plot(df_line.index, df_line['value'], color='red', linewidth=1)
    
    # Set labels and title
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.groupby([df_bar.index.year, df_bar.index.month]).mean().rename(columns={"value": "Average Page Views"})
    df_bar.index.names = ['Years', 'Month']
    df_bar = df_bar.reset_index()
    df_bar['Month'] = pd.to_datetime(df_bar['Month'], format='%m').dt.month_name()

    # Draw bar plot
    hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    g = sns.catplot(
        data=df_bar,
        kind='bar',
        x='Years',
        y='Average Page Views',
        hue="Month",
        hue_order=hue_order,
        palette=sns.color_palette(),
        height=6,
        aspect=1.5
    )

    # Get the legend
    legend = g.legend
    
    # Set title of legend
    legend.set_title("Months")

    # Move legend inside the plot (top-left)
    legend.set_bbox_to_anchor((0.11, 0.97))
    legend._loc = 2  # 2 = upper left

    # Add border around the legend
    legend.set_frame_on(True)

    # Loop over each Axes in the FacetGrid (even if there is only one)
    for ax in g.axes.flatten():
        # Enable all spines
        for spine in ['top', 'right', 'left', 'bottom']:
            ax.spines[spine].set_visible(True)

    # Save plot to fig variable
    fig = g.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
