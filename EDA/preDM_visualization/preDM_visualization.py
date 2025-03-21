   # final features after narrowing down using filter:
        # hypertension, physical activity - duration, sleep, gender

import matplotlib.pyplot as plt
import seaborn as sns

def preDM_visualization(preDM_filter):

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

    plt.tight_layout()

    # 2. compare physical activity and sleep by hypertension status 
        # helps compare distributions of sleep & activity between hypertensive vs. 
        # non-hypertensive individuals.
    plt.figure(figsize=(12, 6))

    # Physical Activity vs Hypertension
    plt.subplot(1, 2, 1)
    sns.boxplot(x="BPQ020", y="PADDURAT", data=preDM_filter, palette="coolwarm", hue="BPQ020", legend=False)
    plt.title("Pre-DM filtered Data: Physical Activity Duration vs Hypertension")
    plt.suptitle("Filter values: Plasma fasting insulin levels ≥ 100 mg/dl OR ApoB levels ≥ 110 mg/dl OR HbA1c ≥ 5.5%", fontsize=10, y=0.98)
    plt.xlabel("Hypertension (0=No, 1=Yes)")
    plt.ylabel("Physical Activity Duration (minutes)")

    # Sleep vs Hypertension
    plt.subplot(1, 2, 2)
    sns.boxplot(x="BPQ020", y="SLD010H", data=preDM_filter, palette="coolwarm", hue="BPQ020", legend=False)
    plt.title("Pre-DM filtered Data: Sleep Duration vs Hypertension")
    plt.suptitle("Filter values: Plasma fasting insulin levels ≥ 100 mg/dl OR ApoB levels ≥ 110 mg/dl OR HbA1c ≥ 5.5%", fontsize=10, y=0.98)
    plt.xlabel("Hypertension (0=No, 1=Yes)")
    plt.ylabel("Sleep Duration (hours)")

    plt.tight_layout()

    # 3. visualize relationship between physical activity & sleep by hypertension status
        # shows if people with hypertension tend to have lower activity/sleep durations.
    plt.figure(figsize=(8, 6))

    sns.scatterplot(data=preDM_filter, x="PADDURAT", y="SLD010H", hue="BPQ020", palette="coolwarm", alpha=0.7)
    plt.title("Pre-DM filtered Data: Physical Activity vs Sleep Duration (Colored by Hypertension)")
    plt.suptitle("Filter values: Plasma fasting insulin levels ≥ 100 mg/dl OR ApoB levels ≥ 110 mg/dl OR HbA1c ≥ 5.5%", fontsize=10, y=0.98)
    plt.xlabel("Physical Activity Duration (minutes)")
    plt.ylabel("Sleep Duration (hours)")
    plt.legend(title="Hypertension", labels=["No", "Yes"])
    plt.tight_layout()

    # 4. density of sleep/activity duration by hypertension status
        # smoother than a histogram, good for distribution insights.
    plt.figure(figsize=(12, 5))

    # Histogram for Physical Activity
    plt.subplot(1, 2, 1)
    sns.histplot(data=preDM_filter, x="PADDURAT", hue="BPQ020", bins=30, fill=True, palette="coolwarm")
    plt.title("Pre-DM filtered Data: Physical Activity by Hypertension")
    plt.suptitle("Filter values: Plasma fasting insulin levels ≥ 100 mg/dl OR ApoB levels ≥ 110 mg/dl OR HbA1c ≥ 5.5%", fontsize=10, y=0.98)
    plt.xlabel("Physical Activity Duration (minutes)")

    # KDE for Sleep Duration
    plt.subplot(1, 2, 2)
    sns.kdeplot(data=preDM_filter, x="SLD010H", hue="BPQ020", fill=True, palette="coolwarm")
    plt.suptitle("Filter values: Plasma fasting insulin levels ≥ 100 mg/dl OR ApoB levels ≥ 110 mg/dl OR HbA1c ≥ 5.5%", fontsize=10, y=0.98)
    plt.title("Pre-DM filtered Data: Density of Sleep Duration by Hypertension")
    plt.xlabel("Sleep Duration (hours)")
    plt.tight_layout()
      
    # 5. pair plot for preDM_filtered datawith hypertension as hue

    #custom labels for pair plot
    custom_labels = {
        "BPQ020": "Hypertension (Yes/No)",
        "PADDURAT": "Physical Activity (Minutes)",
        "SLD010H": "Sleep Duration (Hours)",
        "RIAGENDR": "Gender (Male=1, Female=2)"
    }
    
    hue_labels = {2: "No Hypertension", 1: "Yes Hypertension"}
    preDM_filter.loc[:, "BPQ020"] = preDM_filter["BPQ020"].map(hue_labels).astype("object")

    g = sns.pairplot(preDM_filter[["PADDURAT", "SLD010H", "BPQ020", "RIAGENDR"]], hue="BPQ020")

    for ax in g.axes.flat:
        if ax is not None: 
            # replace x-label if it's in our custom labels
            if ax.get_xlabel() in custom_labels:
                ax.set_xlabel(custom_labels[ax.get_xlabel()], fontsize=10, labelpad=15)
            # replace y-label if it's in our custom labels
            if ax.get_ylabel() in custom_labels:
                ax.set_ylabel(custom_labels[ax.get_ylabel()], fontsize=10, labelpad=15)

    plt.xticks(rotation=30)  # Rotate x-axis labels
    plt.yticks(rotation=30)  # Rotate y-axis labels

    plt.suptitle("Pairplot of Pre-DM Filtered Data by Hypertension", fontsize=10, y=1.00)

    plt.show()

