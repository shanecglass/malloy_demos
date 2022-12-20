# Google Political Ads
Google supports responsible political advertising in the United States through several steps, but the most important of these is transparency into who is purchasing ads through our advertising platform. You can learn more about the [Political Ads Transparency Report](https://adstransparency.google.com/political?political&region=US) by visiting their website or start analyzing the data in BigQuery through the [BigQuery Public Datasets Program](https://console.cloud.google.com/marketplace/product/transparency-report/google-political-ads).

-## What is this?

[Malloy Composer](https://github.com/malloydata/malloy-composer) is an open source tool for viewing and exploring data sets.  Data models are created in the [Malloy](https://malloydata.github.io/malloy/documentation/) language.  Data can be served from a simple webserver or from a SQL database.

See the [Malloy source code](https://github.com/lloydtabb/baby_names/)


## Summary dashboard

Use the dashboard below to get a summary of political ad purchases by advertiser.

<!-- malloy-query
name="Summary Dashboard"
description="Advertiser Summary Dashboard"
model="./google_ads.malloy"
renderer="dashboard"
-->
```malloy
  query: creative_stats -> top_line_dashboard
```
## Deep dive queries
Use the queries below to dig into further detail about a specific topic that interests you. Add filters to see a more granular slice of the queries provided.
<!-- malloy-query
name="Spend over time"
description="Explore how ad spending has evolved month over month"
model="./google_ads.malloy"
-->
```malloy
  query: creative_stats -> spend_over_time
```

<!-- malloy-query
name="Spend by media type"
description="Explore how ad spending broke down by ad type"
model="./google_ads.malloy"
-->
```malloy
  query: creative_stats -> spend_by_media_type
```

<!-- malloy-query
name="Recent ads"
description="The ten most recent ads that generated at least 1 impression"
model="./google_ads.malloy"
-->
```malloy
  query: creative_stats -> recent_ads
```

<!-- malloy-query
name="Most expensive ads"
description="The ten expensive ads that generated at least 1 impression. Add a filter to see this list for each individual advertiser"
model="./google_ads.malloy"
-->
```malloy
  query: creative_stats -> top_lifetime_spend
```
