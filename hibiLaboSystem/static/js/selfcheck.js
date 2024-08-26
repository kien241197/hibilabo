$(document).ready(function () {

    const tab = $(".tab");
    const hash = window.location.hash;

    tab.css("display", "none");

    if (hash === "#selfcheck_type" || !hash) {

        $(`#tab0`).css("display", "block");
        $('.selfcheck_nav').eq(0).addClass('active')
    }

    if (hash === "#selfcheck_type_chart") {

        $(`#tab1`).css("display", "block");
        $('.selfcheck_nav').eq(1).addClass('active')
    }

    if (hash === "#selfcheck_index") {

        $(`#tab2`).css("display", "block");
        $('.selfcheck_nav').eq(2).addClass('active')
    }

    if (hash === "#selfcheck_index_chart") {

        $(`#tab3`).css("display", "block");
        $('.selfcheck_nav').eq(3).addClass('active')
    }

    if (hash === "#selfcheck_questions") {

        $(`#tab4`).css("display", "block");
        $('.selfcheck_nav').eq(4).addClass('active')
    }

    $(".selfcheck_nav").click(function () {

        const index = $(this).closest("li").index();

        tab.css("display", "none");
        $(".selfcheck_nav").removeClass("active");

        $(`#tab${index}`).css("display", "block");
        $(this).addClass("active");
    })

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $("#myForm").submit(function (event) {

        event.preventDefault()

        const evaluation_unit = $(this).find('select[name="evaluation_unit"]').val()
        const user_id = $(this).find('select[name="user_id"]').val()

        const csrftoken = getCookie('csrftoken')

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlSelfCheckTypeAjax,
            data: {
                user_id,
                evaluation_unit,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {

                let html = "";

                if (res?.context?.result_queryset) {

                    res.context.result_queryset.map((item, index) => {

                        html += `
                            <tr>
                                <td>${index}</td>
                                <td style="text-wrap: nowrap;">
                                    ${visbleFlag ? item.full_name : ''}
                                </td>
                                <td>${item.selfcheck_circl}</td>
                                <td>${item.selfcheck_square}</td>
                                <td>${item.selfcheck_traiangle}</td>
                            </tr>
                        `
                    })

                    $(".tbody-tab-1").html(html)
                } else {

                    $(".tbody-tab-1").html(html)
                }

            },
            error: function (error) {

                console.log(error);
            }
        })

    })

    $("#myForm1").submit(function (event) {

        event.preventDefault()

        const evaluation_unit = $(this).find('select[name="evaluation_unit"]').val()
        const user_id = $(this).find('select[name="user_id"]').val()

        const csrftoken = getCookie('csrftoken')

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlSelfCheckTypeChartAjax,
            data: {
                user_id,
                evaluation_unit,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {

                let html = ''
                if (res?.context?.result_queryset) {

                    res.context.result_queryset.map((item, index) => {

                        html += `
                            <div>
                                <div class="images">
                                    ${visbleFlag ? `<p>${item.full_name}</p>` : ""}
                                    <canvas id="mycanvas1-${item.user_id}"></canvas>
                                </div>
                            </div>
                            `
                    })

                    $(".content-chart-tab-1").html(html)

                    res.context.result_queryset.map(item => {

                        const type_list = [item.selfcheck_circl, item.selfcheck_square, item.selfcheck_traiangle]
                        create_chart1(item.user_id, type_list)
                    })
                } else {

                    $(".content-chart-tab-1").html(html)
                }
            },
            error: function (error) {

                console.log(error);
            }
        })
    })

    $("#myForm2").submit(function (event) {

        event.preventDefault()

        const evaluation_unit = $(this).find('select[name="evaluation_unit"]').val()
        const user_id = $(this).find('select[name="user_id"]').val()

        const csrftoken = getCookie('csrftoken')

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlSelfcheckIndexAjax,
            data: {
                user_id,
                evaluation_unit,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {

                let html = "";

                if (res?.context?.result_queryset) {

                    res?.context?.result_queryset.map((item, index) => {

                        html += `
                            <tr>
                                <td>${index + 1}</td>
                                <td class="text-nowrap text-center">
                                    ${visbleFlag ? item.full_name : ''}
                                </td>
                                <td class="text-center">${item.sum_selfcheck_index}</td>
                                <td class="text-center">${item.selfcheck_index1}</td>
                                <td class="text-center">${item.selfcheck_index2}</td>
                                <td class="text-center">${item.selfcheck_index3}</td>
                                <td class="text-center">${item.selfcheck_index4}</td>
                                <td class="text-center">${item.selfcheck_index5}</td>
                                <td class="text-center">${item.selfcheck_index6}</td>
                                <td class="text-center">${item.selfcheck_index7}</td>
                                <td class="text-center">${item.selfcheck_index8}</td>
                                <td class="text-center">${item.selfcheck_index9}</td>
                                <td class="text-center">${item.selfcheck_index10}</td>
                                <td class="text-center">${item.selfcheck_index11}</td>
                                <td class="text-center">${item.selfcheck_index12}</td>
                            </tr>
                        `
                    })

                    $(".tbody-table-tab-2").html(html)
                } else {

                    $(".tbody-table-tab-2").html(html)
                }

            },
            error: function (error) {

                console.log(error);
            }
        })

    })

    $("#myForm3").submit(function (event) {

        event.preventDefault()

        const evaluation_unit = $(this).find('select[name="evaluation_unit"]').val()
        const user_id = $(this).find('select[name="user_id"]').val()

        const csrftoken = getCookie('csrftoken')

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlSelfcheckIndexChartAjax,
            data: {
                user_id,
                evaluation_unit,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {

                let html = "";
                if (res?.context?.result_queryset) {
                    // script>window.onload=create_chart2({{ record.user.id }}, {{ record.index_list|safe }})</script>
                    res.context.result_queryset.map(item => {

                        html += `
                            <div>
                                <div class="images"  style="width: 320px; height: 320px;">
                                ${visbleFlag ? `<p>${item.full_name}</p>` : ''}
                                <canvas id="mycanvas-${item.user_id}"></canvas>
                                </div>
                            </div>
                        `
                    })

                    $(".chart-tab-3").html(html)

                    res.context.result_queryset.map(item => {

                        create_chart2(item.user_id, [item.selfcheck_index1, item.selfcheck_index2, item.selfcheck_index3, item.selfcheck_index4, item.selfcheck_index5, item.selfcheck_index6, item.selfcheck_index7, item.selfcheck_index8, item.selfcheck_index9, item.selfcheck_index10, item.selfcheck_index11, item.selfcheck_index12])
                    })
                } else {

                    $(".chart-tab-3").html(html)
                }


            },
            error: function (error) {

                console.log(error);
            }
        })
    })

    $("#myForm4").submit(function (event) {

        event.preventDefault()

        const evaluation_unit = $(this).find('select[name="evaluation_unit"]').val()
        const user_id = $(this).find('select[name="user_id"]').val()
        const selfcheck_role = $(this).find('select[name="selfcheck_role"]').val()

        const csrftoken = getCookie('csrftoken')

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlSelfcheckQuestionAjax,
            data: {
                user_id,
                evaluation_unit,
                selfcheck_role,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {

                let htmlTH = '<th>No.</th><th>質問</th>'
                let htmlTR = ''

                if (res?.context?.staff_list?.length > 0 & res?.context?.qr_list?.length > 0) {

                    res.context.staff_list.map((item) => {

                        htmlTH += `<th>${visbleFlag ? item.name : ''}</th>`
                    })

                    $('.user_name_tab4').html(htmlTH);

                    res.context.qr_list.map((item, index) => {

                        let row = `<tr>`;
                        row += `<td class="tatefixed">${index + 1}</td>`;

                        item.forEach((value, index) => {
                            row += `<td class="tatefixed ${index === 0 ? 'text-left' : ''}">${value}</td>`;
                        });

                        row += `</tr>`;
                        htmlTR += row;
                    });

                    $(".tbody-tab4").html(htmlTR)
                } else {

                    $('.user_name_tab4').html(htmlTH);
                    $(".tbody-tab4").html(htmlTR)
                    $(".message").html("データがありません")

                }
            },
            error: function (error) {

                console.log(error);
            }
        })
    })
    function create_chart1(id, data) {

        var strname = "mycanvas1-" + id;

        //図を動的に生成
        var ctx = document.getElementById(strname);

        createChart(ctx, data, false)
    }

    function create_chart2(id, data) {

        var strname = "mycanvas-" + id;
    
        //図を動的に生成
        var ctx = document.getElementById(strname);
    
        chart(ctx, data, false)
    }
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

function createChartSample1() {

    var strname = "mycanvas-sample"
    var ctx = document.getElementById(strname);

    createChart(ctx, [6, 3, 7], true)
}