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
    df_bar = df.copy().reset_index()
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]

    # It should show average daily page views for each month grouped by year. 
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()#.reset_index()
    df_bar = df_bar.unstack()
    #columns
    df_bar.columns = ['January','February','March','April','May','June','July','August','September','October','November','December']
    # Draw bar plot
    fig = df_bar.plot(kind= 'bar', figsize = (15,10)).figure

    plt.title('')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title= 'Months', fontsize = 15)

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
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

    # Set correct month order for month-wise box plot
    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw year-wise box plot
    sns.boxplot(data=df_box, x='year', y='value', palette=sns.color_palette(), ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    # Draw month-wise box plot
    sns.boxplot(data=df_box, x='month', y='value', palette='pastel', order=order, ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
