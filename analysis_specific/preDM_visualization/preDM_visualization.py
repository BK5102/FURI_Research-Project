import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def preDM_visualization(preDM_filter):
    # final features after narrowing down using filter:
        # hypertension, physical activity - duration, sleep, gender

    final_features = ['BPQ020', 'PADDURAT', 'SLD010H', 'RIAGENDR']
    #numeric_cols = preDM_filter[final_features].select_dtypes(include=[float, int]).columns

    # 1. compare hypertension rates by gender 
        # shows how many males vs. females reported hypertension.
    # Count hypertension cases by gender
    hypertension_counts = preDM_filter.groupby("RIAGENDR")["BPQ020"].value_counts().unstack()

    # Plot
    hypertension_counts.plot(kind="bar", figsize=(8,5), colormap="coolwarm")
    plt.title("Pre-DM filtered Data: Hypertension by Gender")
    plt.suptitle("Filter values: Plasma fasting insulin levels ≥ 100 mg/dl OR ApoB levels ≥ 110 mg/dl OR HbA1c ≥ 5.5%", fontsize=10, y=0.98)
    plt.xlabel("Gender (1=Male, 2=Female)")
    plt.ylabel("Count")
    plt.legend(["No Hypertension", "Yes Hypertension"])
    plt.xticks(rotation=0)
    #plt.show()


    # 2. compare physical activity and sleep by hypertension status 
        # helps compare distributions of sleep & activity between hypertensive vs. 
        # non-hypertensive individuals.
    plt.figure(figsize=(12, 6))

    # Physical Activity vs Hypertension
    plt.subplot(1, 2, 1)
    sns.boxplot(x="BPQ020", y="PADDURAT", data=preDM_filter, palette="coolwarm")
    plt.title("Pre-DM filtered Data: Physical Activity Duration vs Hypertension")
    plt.suptitle("Filter values: Plasma fasting insulin levels ≥ 100 mg/dl OR ApoB levels ≥ 110 mg/dl OR HbA1c ≥ 5.5%", fontsize=10, y=0.98)
    plt.xlabel("Hypertension (0=No, 1=Yes)")
    plt.ylabel("Physical Activity Duration (minutes)")

    # Sleep vs Hypertension
    plt.subplot(1, 2, 2)
    sns.boxplot(x="BPQ020", y="SLD010H", data=preDM_filter, palette="coolwarm")
    plt.title("Pre-DM filtered Data: Sleep Duration vs Hypertension")
    plt.suptitle("Filter values: Plasma fasting insulin levels ≥ 100 mg/dl OR ApoB levels ≥ 110 mg/dl OR HbA1c ≥ 5.5%", fontsize=10, y=0.98)
    plt.xlabel("Hypertension (0=No, 1=Yes)")
    plt.ylabel("Sleep Duration (hours)")

    plt.tight_layout()
    plt.show()


    # 3. visualize relationship between physical activity & sleep by hypertension status
        # shows if people with hypertension tend to have lower activity/sleep durations.


    # 4. density of sleep/activity duration by hypertension status
        # smoother than a histogram, good for distribution insights.

