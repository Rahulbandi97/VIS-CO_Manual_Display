import streamlit as st
from PIL import Image

# Define the main title of the app
st.title("VIS-CO")

# Sidebar for selecting the category
category = st.sidebar.selectbox("Select a Category", ["Finance", "Health"])

# Define dictionaries containing queries and their corresponding image filenames for each category
queries = {
    "Finance": {
        "Relationship Between Total Income and Credit Amount": "relationship_between_total_income_and_credit_amount.png",
        "Count of Loans by Number of Children": "count_of_loans_by_the_number_of_children.png",
        "Income Levels by Type of Employment": "income_levels_by_type_of_employment.png",
        "Distribution of loan purposes (like education, renovation, etc.)": "distribution_of_loan_purposes.png",
        "Correlation Between Loan Amount and Client Age": "correlation_between_loan_amount_and_client_age.png",
        "Loan Performance by Gender": "loan_performance_by_gender.png",
        "Effect of Owning a Car on Loan Performance": "effect_of_owning_a_car_on_loan_performance.png",
        "Loan Performance by Loan Type": "loan_performance_by_loan_type.png",
        "Influence of Marital Status on Loan Amount": "influence_of_marital_status_on_loan_amount.png",
        "Age Distribution of Clients with Payment Difficulties": "age_distribution_of_clients_with_payment_difficulties.png"
    },
    "Health": {
        "Distribution of Plans by Metal Level":"distribution_of_plans_by_metal_level.png",
        "Average Premiums by State":"average_individual_premiums_by_state.png",
        "Plan Availability by County":"heatmap_of_plan_availability_by_county.png",
        "Out-of-Pocket Costs by Plan Type":"max_out_of_pocket_by_plan_type.png",
        "Issuer Market Share":"number_of_plans_by_each_issue.png",
        "Distribution of Specific Benefits (e.g., dental coverage) by Plan":"dental_coverage_by_plan_type.png",
        "Comparison of Deductibles Across States":"medical_deductable_by_state.png",
        "Impact of Metal Level on Deductibles and Out-of-Pocket Maximums":"deductibles_and_out_of_pocket_maximums_by_metal_level.png",
        "Relationship Between Premiums and Out-of-Pocket Maximums":"premium_by_out_of_pocket_maximum.png"
    }
}

# Dropdown to select a query based on the selected category
if category:
    selected_query = st.sidebar.selectbox("Select a Query", list(queries[category].keys()))

# Handling the submit button to show images
if st.button("Show Results"):
    if selected_query:
        # Retrieve the filename for the selected query
        filename = queries[category][selected_query]
        image_path = f"images/{category.lower()}/{filename}"

        # Load and display the image
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"Graph for {selected_query}")
        except FileNotFoundError:
            st.error("Image not found for the selected query.")
