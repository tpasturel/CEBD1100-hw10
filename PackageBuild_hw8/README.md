The sklearn wine dataset contains 178 numeric observations for 13 attributes for 3 wine grape types. This package allows to plot and compare this dataset's attributes by pairs (e.g. two columns at a time).

The file contains the following columns (one per attribute): alcalinity_of_ash alcohol ash color_intensity flavanoids hue magnesium malic_acid nonflavanoid_phenols od280/od315_of_diluted_wines proanthocyanins proline target total_phenols

======== Instructions on how to use the script ========
1. Import the module to your script
from CEBD1100hw8ThibaultPasturel_pkg import CEBD1100homework8ThibaultPasturel as mod

2. Properly call the module in your script
mod.main()


3. Print all column names in order to select the pair you want to compare python 
python yourscript -H

4. Scatter the two columns in order to see the potential correlation between the two compared attributes per grape type 
python yourscript -c1 <column_name_1> -c <column_name_2> 
example: python yourscript -c1 ash -c2 alcohol
