function initViz() {
    var containerDiv = document.getElementById("vizContainer"),
    url = "https://public.tableau.com/views/EmbedTest_16606360562240/ProfitDashboard?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link";

    var viz = new tableau.Viz(containerDiv, url);
}