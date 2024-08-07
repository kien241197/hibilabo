$(document).ready(function () {

    const tab = $(".tab");
    const hash = window.location.hash;

    tab.css("display", "none");

    if (hash === "#selfcheck_type" || !hash) {

        $(`#tab0`).css("display", "block");
        $('.honne-nav').eq(0).addClass('active')
    }

    if (hash === "#selfcheck_type_chart") {

        $(`#tab1`).css("display", "block");
        $('.honne-nav').eq(1).addClass('active')
    }

    if (hash === "#selfcheck_index") {

        $(`#tab2`).css("display", "block");
        $('.honne-nav').eq(2).addClass('active')
    }

    if (hash === "#selfcheck_index_chart") {

        $(`#tab3`).css("display", "block");
        $('.honne-nav').eq(3).addClass('active')
    }

    if (hash === "#selfcheck_questions") {

        $(`#tab4`).css("display", "block");
        $('.honne-nav').eq(4).addClass('active')
    }

    $(".honne-nav").click(function () {

        const index = $(this).closest("li").index();

        tab.css("display", "none");
        $(".honne-nav").removeClass("active");

        $(`#tab${index}`).css("display", "block");
        $(this).addClass("active");
    })
})

function chart(ctx, data, labels) {

    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: labels ? ['決断力', '専門性', '自己管理', '広報力', '連携力', '人間関係', '患者対応', 'チームワーク力', '総合管理', '理念浸透', '自己啓発', '思考'] : ['', '', '', '', '', '', '', '', '', '', '', ''],
            datasets: [{
                label: '',
                data: data,
                // データライン
                borderColor: 'yellow',
                borderWidth: 4,
            }],
        },
        options: {
            //タイトル消
            plugins: {
                legend: {
                    display: false
                },
                //https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#anchoring
                datalabels: {
                    font: {
                        size: 20
                    },
                },
            },
            scales: {
                r: {
                    //メモリ線
                    ticks: {
                        display: false
                    },
                    // 最小値・最大値
                    min: 0,
                    max: 15,
                    // 背景色
                    backgroundColor: 'darkgray',
                    // グリッドライン
                    grid: {
                        color: 'gainsboro',
                    },
                    // アングルライン
                    angleLines: {
                        color: 'darkgray',
                    },
                    // ポイントラベル
                    pointLabels: {
                        color: 'black',
                        backdropColor: '#ffffff',
                        backdropPadding: 5,
                        padding: 20,
                    },
                },
            },
        },
    });
}

function create_chart2(id, data) {

    var strname = "mycanvas-" + id;

    //図を動的に生成
    var ctx = document.getElementById(strname);

    chart(ctx, data, false)
}

function createChartSample2() {

    var strname = "mycanvas-spamle";
    var ctx = document.getElementById(strname);

    chart(ctx, [2, 4, 4, 7, 2, 1, 4, 7, 3, 2, 1, 5], true)
}


function createChart(ctx, data, labels) {

    new Chart(ctx, {
        type: 'radar',
        data: {
            // ラベルも本当は動的にすべき
            labels: labels ? ['人に合わせられるタイプ', 'バランスタイプ', '感情を大切にするタイプ'] : ["", "", ""],
            datasets: [{
                label: '',
                // データも本当は動的にすべき
                data: data,
                // データライン
                borderColor: 'yellow',
                borderWidth: 4,
            }],
        },
        options: {
            //タイトル消
            plugins: {
                legend: {
                    display: false
                },
                //https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#anchoring
                datalabels: {
                    font: {
                        size: 20
                    },
                },
            },
            scales: {
                r: {
                    //メモリ線
                    ticks: {
                        display: false
                    },
                    // 最小値・最大値
                    min: 0,
                    max: 60,
                    // 背景色
                    backgroundColor: 'darkgray',
                    // グリッドライン
                    grid: {
                        color: 'gainsboro',
                    },
                    // アングルライン
                    angleLines: {
                        color: 'darkgray',
                    },
                    // ポイントラベル
                    pointLabels: {
                        color: 'black',
                        backdropColor: '#ffffff',
                        backdropPadding: 5,
                        padding: 20,
                    },
                },
            },
        },
    });

}
function create_chart1(id, data) {

    var strname = "mycanvas-" + id;

    //図を動的に生成
    var ctx = document.getElementById(strname);

    createChart(ctx, data, false)
}

function createChartSample1() {

    var strname = "mycanvas-sample"
    var ctx = document.getElementById(strname);

    createChart(ctx, [6, 3, 7], true)
}