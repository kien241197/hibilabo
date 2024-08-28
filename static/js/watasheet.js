function func_count_type(element) {
    let group = $(element).data('group');
    if ($(element).is(":checked")) {
        typeList[group] += 1;
    } else {
        typeList[group] -= 1;
    }
    for (var type in typeList) {
        if (typeList.hasOwnProperty(type)) {
            $(`#type_${type}`).text(typeList[type]);
        }
    }
}

function auto_grow(element) {
    element.style.height = "5px";
    element.style.height = (element.scrollHeight) + "px";

    let pairs = [1, 2, 3, 4, 5, 6, 7, 8, 9];

    pairs.forEach(function (pair) {
        let elements = $(`.items[data-pair="${pair}"]`);

        elements.css('min-height', 0);
    });
}

$(document).ready(function () {

    const hashValue = window.location.hash;
    const cleanHashValue = hashValue.slice(1);

    $('.tab-pane fade').removeClass('show active');
    $('.button-tab').removeClass('active');

    if (cleanHashValue === "tab-1" || cleanHashValue === "tab-2" || cleanHashValue === "tab-3") {

        $("input[name='最終提出']").css("display", "none");
        $(".wrapper-最終提出").css("display", "none");
    } else {

        $("input[name='最終提出']").css("display", "block");
        $(".wrapper-最終提出").css("display", "flex");

    }

    if (cleanHashValue === "tab-2" || cleanHashValue === "tab-3") {

        $('#modal').css("display", 'block')

        if (cleanHashValue === "tab-2") {

            $('#image-modal').attr('src', '/static/assets/images/modal-watasheet-tab-2.png')
        } else {

            $('#image-modal').attr('src', '/static/assets/images/modal-watasheet-tab-3.png')
        }
    } else {

        $('#modal').css("display", 'none')
    }

    if (cleanHashValue === "team-concept" || !hashValue) {
        $('.container-checkbox').addClass("hidden")
        $('.nav-tab-0').addClass("active")
        $('.nav-tab-0').css("color", "white")
        $('#nav-0').addClass('show active');
        $('.title-tab').text("TEAM CONCEPT");
        $('.desc-tab').html("会社 ・ チームとしての方向性の共有");
        $('.title-tab-h3').text("");
        $('.desc-tab-p').text("");
    }

    if (cleanHashValue === "my-concept") {

        $(".nav-tab-my").addClass("active")
        $('.nav-tab-my').css("color", "white")
        $("#nav-my").addClass("show active")
        $('.title-tab').text("MY CONCEPT");
        $('.desc-tab').html("わたしの方向性・芯");
        $('.title-tab-h3').text("");
        $('.desc-tab-p').text("");
    }

    if (cleanHashValue === "tab-1") {

        $(".nav-tab-3").addClass("active")
        $('.nav-tab-3').css("color", "white")
        $("#nav-3").addClass("show active")
        $('.title-tab').text(`PROFESSIONAL TYPE ${30}`);
        $('.desc-tab').text("わたしが望んでいる仕事を知る");
        $('.title-tab-h3').text("INTEREST");
        $('.desc-tab-p').text("リストアップされている項目の中から自身が求めていると思うものの□にチェックを入れてください （複数チェック可）");
    }

    if (cleanHashValue === "tab-2") {

        $(".nav-tab-4").addClass("active")
        $('.nav-tab-4').css("color", "white")
        $("#nav-4").addClass("show active")
        $('.title-tab').text("KNOW MY SELF");
        $('.desc-tab').html("私の●●を 3 つのポイントにまとめていきます。<br/> （＊ひとつのポイントでも多くても構いません）<br/> ＊自分の人生において仕事、 私事を含め記入してください <br/> （ライフワークバランス） <br/> ＊自分の書きやすい項目から記入可能です");
        $('.title-tab-h3').text("");
        $('.desc-tab-p').text("");

    }

    if (cleanHashValue === "tab-3") {

        $(".nav-tab-5").addClass("active")
        $('.nav-tab-5').css("color", "white")
        $("#nav-5").addClass("show active")
        $('.title-tab').text("KNOW MY SELF");
        $('.desc-tab').html("私の●●を 3 つのポイントにまとめていきます。<br/> （＊ひとつのポイントでも多くても構いません）<br/> ＊自分の人生において仕事、 私事を含め記入してください <br/> （ライフワークバランス） <br/> ＊自分の書きやすい項目から記入可能です");
        $('.title-tab-h3').text("");
        $('.desc-tab-p').text("");
    }

    if (cleanHashValue === "tab-4") {

        $(".nav-tab-8").addClass("active")
        $('.nav-tab-8').css("color", "white")
        $("#nav-8").addClass("show active")
        $('.title-tab').text("MY TIME LINE");
        $('.desc-tab').html("わたしの過去 ・ 現在 ・ 未来の年表を作ってみましょう！");
        $('.title-tab-h3').text("");
        $('.desc-tab-p').text("");
    }

    if (!cleanHashValue) {
        $('.container-checkbox').addClass("hidden")

    } else if ((cleanHashValue !== "team-concept" && cleanHashValue !== "my-concept")) {
        $('.container-checkbox').removeClass("hidden")
    }

    // Xử lý sự kiện click cho các button tab
    $('.button-tab').click(function () {

        setTimeout(() => {
            adjustHeight();
        }, 300)
        // Loại bỏ class active từ tất cả các button tab
        $('.button-tab').removeClass('active');

        // Thêm class active cho button tab được click
        const text = $(this).attr('id')

        $(`#${text}`).addClass('active');
        $(`.${text}`).addClass('active');

        if (text == 'nav-tab-3') {

            $('.title-tab').text(`PROFESSIONAL TYPE ${30}`);
            $('.desc-tab').text("わたしが望んでいる仕事を知る");
            $('.title-tab-h3').text("INTEREST");
            $('.desc-tab-p').text("リストアップされている項目の中から自身が求めていると思うものの□にチェックを入れてください （複数チェック可）");
            $("input[name='最終提出']").css("display", "none");
            $(".wrapper-最終提出").css("display", "none");
        } else if (text === 'nav-tab-0') {

            $('.title-tab').text("TEAM CONCEPT");
            $('.desc-tab').html("会社 ・ チームとしての方向性の共有");
            $('.title-tab-h3').text("");
            $('.desc-tab-p').text("");
            $('.container-checkbox').addClass("hidden")
        } else if (text === "nav-tab-8") {

            $('.title-tab').text("MY TIME LINE");
            $('.desc-tab').html("わたしの過去 ・ 現在 ・ 未来の年表を作ってみましょう！");
            $('.title-tab-h3').text("");
            $('.desc-tab-p').text("");
            $("input[name='最終提出']").css("display", "block");
            $(".wrapper-最終提出").css("display", "flex");
        } else if (text === 'nav-tab-my') {

            $('.title-tab').text("MY CONCEPT");
            $('.desc-tab').html("わたしの方向性・芯");
            $('.title-tab-h3').text("");
            $('.desc-tab-p').text("");
            $('.container-checkbox').addClass("hidden")

        } else {

            $('.title-tab').text("KNOW MY SELF");
            $('.desc-tab').html("私の●●を 3 つのポイントにまとめていきます。<br/> （＊ひとつのポイントでも多くても構いません）<br/> ＊自分の人生において仕事、 私事を含め記入してください <br/>（ライフワークバランス） <br/> ＊自分の書きやすい項目から記入可能です");
            $('.title-tab-h3').text("");
            $('.desc-tab-p').text("");
            $("input[name='最終提出']").css("display", "none");
            $(".wrapper-最終提出").css("display", "none");
        }

        if (text !== "nav-tab-0" && text !== "nav-tab-my") {

            $('.container-checkbox').removeClass("hidden")
        }

        $('.button-tab').css("color", "#727171")
        $(`.${text}`).css("color", "white")

        if (text === 'nav-tab-4' || text === 'nav-tab-5') {

            $('#modal').css("display", 'block')

            if (text === 'nav-tab-4') {

                $('#image-modal').attr('src', '/static/assets/images/modal-watasheet-tab-2.png')
            } else {

                $('#image-modal').attr('src', '/static/assets/images/modal-watasheet-tab-3.png')
            }
        } else {

            $('#modal').css("display", 'none')
        }
    });

    $('.textarea-watasheet').each(function () {

        const textarea = $(this);
        const text = textarea.val();

        const lineCount = (text.match(/\n/g) || []).length + 1;

        textarea.attr('rows', lineCount || 1);
    });

    function adjustHeight() {
        if (window.innerWidth > 600) {
            let pairs = [1, 2, 3, 4, 5, 6, 7, 8, 9];

            pairs.forEach(function (pair) {
                let elements = $(`.items[data-pair="${pair}"]`);
                let maxHeight = 0;

                elements.each(function () {
                    var thisHeight = $(this).outerHeight();
                    if (thisHeight > maxHeight) {
                        maxHeight = thisHeight;
                    }
                });
                elements.css('min-height', maxHeight);
            });
        }
    }

    const observer = new MutationObserver(function (mutations) {
        mutations.forEach(function (mutation) {
            adjustHeight();
        });
    });

    const config = { attributes: true, childList: true, subtree: true };
    $('.items').each(function () {
        observer.observe(this, config);
    });

    // Chạy hàm khi trang được tải lần đầu
    adjustHeight();

    $('#SAMPLE').click(function () {

        setTimeout(() => {

            const hashValue = window.location.hash;
            const cleanHashValue = hashValue.slice(1);

            if (cleanHashValue == "tab-2") {

                $('#tab2').css('display', 'block')
                $('#tab3').css('display', 'none')
            }

            if (cleanHashValue == "tab-3") {

                $('#tab2').css('display', 'none')
                $('#tab3').css('display', 'block')
            }
        }, 200)
    })
});

