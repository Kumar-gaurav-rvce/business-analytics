# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the dashboard
st.title("Business Analytics & Visualization: KPI Dashboard")

# File uploader widget for CSV input
uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

# If a file is uploaded, proceed
if uploaded_file:

    @st.cache_data  # Cache the data loading function for performance
    def load_data(file):
        """
        Reads the uploaded CSV file, parses dates, 
        and creates new time-based & derived columns.
        """
        df = pd.read_csv(file, parse_dates=["Order Date", "Ship Date"])
        
        # Convert to datetime, handling errors gracefully
        df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y', errors='coerce')
        df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y', errors='coerce')

        # Create additional time-based columns
        df['Order_Month'] = df['Order Date'].dt.to_period('M').dt.to_timestamp()
        df['Order_Quarter'] = df['Order Date'].dt.to_period('Q').dt.to_timestamp()
        df['Order_Year'] = df['Order Date'].dt.year

        # Calculate shipping duration in days
        df['Shipping_Duration'] = (df['Ship Date'] - df['Order Date']).dt.days
        
        return df

    # Load the CSV into a DataFrame
    df = load_data(uploaded_file)

    # Ensure required columns are present in the CSV
    required_columns = ['Order Date', 'Ship Date', 'Region', 'Category', 'Sales', 'Segment']
    if not all(col in df.columns for col in required_columns):
        missing_cols = [col for col in required_columns if col not in df.columns]
        st.error(f"Uploaded CSV is missing required columns: {', '.join(missing_cols)}")
    else:
        # Identify numeric columns for KPI selection
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        
        # Sidebar KPI selector (default to 'Sales' if available)
        kpi = st.sidebar.selectbox(
            "Select KPI for analysis:", 
            options=numeric_cols, 
            index=numeric_cols.index('Sales') if 'Sales' in numeric_cols else 0
        )

        # Sidebar aggregation function selector
        agg_func = st.sidebar.selectbox(
            "Select aggregation function:", 
            options=['sum', 'mean', 'max', 'min'], 
            index=0
        )

        # Sidebar time granularity selector
        time_granularity = st.sidebar.selectbox(
            "Group data by:", 
            options=['Month', 'Quarter', 'Year'], 
            index=0
        )

        # Map time granularity selection to column name
        time_map = {
            'Month': 'Order_Month',
            'Quarter': 'Order_Quarter',
            'Year': 'Order_Year'
        }
        time_col = time_map[time_granularity]

        # Sidebar filter options
        st.sidebar.header("Filter Options")
        region_filter = st.sidebar.multiselect(
            "Select Region(s):", 
            options=df['Region'].unique(), 
            default=df['Region'].unique()
        )
        category_filter = st.sidebar.multiselect(
            "Select Category(s):", 
            options=df['Category'].unique(), 
            default=df['Category'].unique()
        )
        segment_filter = st.sidebar.multiselect(
            "Select Segment(s):", 
            options=df['Segment'].unique(), 
            default=df['Segment'].unique()
        )
        date_range = st.sidebar.date_input(
            "Select Order Date Range:",
            [df['Order Date'].min(), df['Order Date'].max()]
        )

        # Apply selected filters to the dataset
        filtered_df = df[
            (df['Region'].isin(region_filter)) &
            (df['Category'].isin(category_filter)) &
            (df['Segment'].isin(segment_filter)) &
            (df['Order Date'] >= pd.to_datetime(date_range[0])) &
            (df['Order Date'] <= pd.to_datetime(date_range[1]))
        ]

        # Calculate the aggregated KPI value
        if agg_func == 'sum':
            total_kpi = filtered_df[kpi].sum()
        elif agg_func == 'mean':
            total_kpi = filtered_df[kpi].mean()
        elif agg_func == 'max':
            total_kpi = filtered_df[kpi].max()
        elif agg_func == 'min':
            total_kpi = filtered_df[kpi].min()
        else:
            total_kpi = filtered_df[kpi].sum()

        # Display the KPI value at the top
        st.metric(f"{agg_func.title()} {kpi}", f"{total_kpi:,.2f}")

        # Group data by selected time granularity and aggregate KPI
        grouped_time = filtered_df.groupby(time_col)[kpi].agg(agg_func)
        
        # Create a line plot of KPI over time
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(grouped_time.index, grouped_time.values, marker='o')
        ax.set_title(f"{agg_func.title()} {kpi} Over Time ({time_granularity})")
        ax.set_xlabel(time_granularity)
        ax.set_ylabel(f"{agg_func.title()} {kpi}")
        ax.grid(True)
        st.pyplot(fig)

        # KPI aggregated by region (bar chart)
        kpi_by_region = filtered_df.groupby('Region')[kpi].agg(agg_func).sort_values(ascending=False)
        st.subheader(f"{agg_func.title()} {kpi} by Region")
        st.bar_chart(kpi_by_region)

        # KPI aggregated by category (bar chart)
        kpi_by_category = filtered_df.groupby('Category')[kpi].agg(agg_func).sort_values(ascending=False)
        st.subheader(f"{agg_func.title()} {kpi} by Category")
        st.bar_chart(kpi_by_category)

        # Display descriptive statistics for the selected KPI
        st.subheader(f"{kpi} Summary Statistics")
        st.write(filtered_df[kpi].describe())

else:
    # Message when no file is uploaded
    st.info("Please upload a CSV file to get started.")
