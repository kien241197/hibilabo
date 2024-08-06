$(document).ready(function () {

    const tab = $(".tab");
    const hash = window.location.hash;

    tab.css("display", "none");

    if (hash === "#honne_total" || !hash) {

        $(`#tab1`).css("display", "block");
        $('.honne-nav').eq(0).addClass('active')
    }

    if (hash === "#honne_type_staticks") {

        $(`#tab1`).css("display", "block");
        $('.honne-nav').eq(1).addClass('active')
    }

    if (hash === "#honne_index_staticks") {

        $(`#tab2`).css("display", "block");
        $('.honne-nav').eq(2).addClass('active')
    }

    if (hash === "#honne_chart") {

        $(`#tab3`).css("display", "block");
        $('.honne-nav').eq(3).addClass('active')
    }

    if (hash === "#honne_qr_staticks") {

        $(`#tab4`).css("display", "block");
        $('.honne-nav').eq(4).addClass('active')
    }

    $(".honne-nav").click(function () {

        const index = $(this).closest("li").index();
        console.log("index", index);

        tab.css("display", "none");
        $(".honne-nav").removeClass("active");


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

        event.preventDefault();

        const evaluation_unit = $(this).find('select[name="evaluation_unit"]').val()
        const csrftoken = getCookie('csrftoken');

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlHonneTotalAjax,
            data: {
                evaluation_unit,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {

                $("#type-a").text(res.context.result.A)
                $("#type-b").text(res.context.result.B)
                $("#type-c").text(res.context.result.C)
                $("#type-d").text(res.context.result.D)
                $("#type_sum").text(res.context.max_type)
            },
            error: function (error) {

                console.log(error);
            }
        })
    });

    $("#myForm1").submit(function (event) {

        event.preventDefault();

        const evaluation_unit = $(this).find('select[name="evaluation_unit"]').val()
        const user_id = $(this).find('select[name="user_id"]').val()

        const csrftoken = getCookie('csrftoken');

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlHonneTypeStaticksAjax,
            data: {
                evaluation_unit,
                user_id,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {

                console.log(res);


                let html = '';


                res?.context?.map((item, index) => {
                    html += `
                    <tr>
                        <td>${index}</td>
                        <td class="text-nowrap">
                            ${showName === 'True' ? item.full_name : ''}
                        </td>
                        <td>${item.kartet_type_a}</td>
                        <td>${item.kartet_type_b}</td>
                        <td>${item.kartet_type_c}</td>
                        <td>${item.kartet_type_d}</td>
                    </tr>`
                })

                $("#tableHonneTypeStaticks").html(html)

            },
            error: function (error) {

                console.log(error);
            }
        })
    })

    $("#myForm2").submit(function (event) {

        event.preventDefault();

        const evaluation_unit = $(this).find('select[name="evaluation_unit"]').val()
        const user_id = $(this).find('select[name="user_id"]').val()

        const csrftoken = getCookie('csrftoken');

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlHonneIndexStaticksAjax,
            data: {
                evaluation_unit,
                user_id,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {

                let html = '';

                res?.context?.map((item, index) => {
                    html += `
                    <tr>
                        <td>${index}</td>
                        <td class="text-center text-nowrap">
                            ${showName === 'True' ? item.full_name : ''}
                        </td>
                        <td>${item.sum_kartet}</td>
                        <td>${item.kartet_index1}</td>
                        <td>${item.kartet_index2}</td>
                        <td>${item.kartet_index3}</td>
                        <td>${item.kartet_index4}</td>
                        <td>${item.kartet_index5}</td>
                        <td>${item.kartet_index6}</td>
                        <td>${item.kartet_index7}</td>
                        <td>${item.kartet_index8}</td>
                    </tr>
                `
                })

                $("#tableIndexTypeStaticks").html(html)

            },
            error: function (error) {

                console.log(error);
            }
        })
    })

    $("#myForm3").submit(function (event) {

        event.preventDefault();

        const evaluation_unit = $(this).find('select[name="evaluation_unit"]').val()
        const user_id = $(this).find('select[name="user_id"]').val()

        const csrftoken = getCookie('csrftoken');

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlHonneChartAjax,
            data: {
                evaluation_unit,
                user_id,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {
                let html = ''
                if (res?.context && res?.context?.length > 0) {
                    res?.context?.map((item, index) => {

                        const data = [item.kartet_index1, item.kartet_index2, item.kartet_index3, item.kartet_index4, item.kartet_index5, item.kartet_index5, item.kartet_index7, item.kartet_index8]

                        html += `
                        <div>
                            <div class="images">
                            <p>
                                ${showName === 'True' ? item.full_name : ''}
                            </p>
                            <div style="width: 400px; height: 400px;">
                                <canvas id="mycanvas-${item.user_id}" style="width: 100%; height: 100%;"></canvas>
                                </div>
                            </div>
                        </div>
                    `
                        $("#imagesHonneChart").html(html)
                        create_graph(item.user_id, data)
                    })
                } else {

                    $("#imagesHonneChart").html(html)
                }


            },
            error: function (error) {

                console.log(error);
            }
        })
    })

    $("#myForm4").submit(function (event) {

        event.preventDefault();

        const evaluation_unit = $(this).find('select[name="evaluation_unit"]').val()
        const user_id = $(this).find('select[name="user_id"]').val()

        const csrftoken = getCookie('csrftoken');

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlHonneQrStaticksAjax,
            data: {
                evaluation_unit,
                user_id,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (res) {

                console.log({ res });


                res.context.staff_list.map((item, index) => {
                    if (showName === 'True') {
                        $('#tableHonneQrStaticks').html(`${item.last_name} ${item.first_name}`)
                    }
                })

                let htmlTbody = ''
                res.context.qr_list.map((item, index) => {
                    console.log(item);

                    htmlTbody += `
                    <tr>
                        <td class="tatefixed">${index}</td>
                        <td class="tatefixed text-left">${item[0]}</td>
                        <td class="tatefixed">${item[1] || ''}</td>
                    </tr>
                `
                })

                $("#tbodyHonneQrStaticks").html(htmlTbody)
            },
            error: function (error) {

                console.log(error);
            }
        })
    })
})