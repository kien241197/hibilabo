function func_count(elem, listQ){
    counter_group = [0,0,0,0,0,0,0,0,0,0,0,0];
    counter_type = [0,0,0];
    listQ.forEach(key => {
        let value = $('#result-'+key).val();
        let arr_index = $('#result-'+key).closest('td').find('#index-'+key).val();
        if(value != '') {
            counter_group[arr_index - 1] += Number(value);
            if (circl.includes(Number(arr_index))) counter_type[0] += Number(value);
            if (square.includes(Number(arr_index))) counter_type[1] += Number(value);
            if (traiangle.includes(Number(arr_index))) counter_type[2] += Number(value);
        }
    })

    //セルフチェックの描画呼び出し
    drwa_chart(counter_group);

    //タイプ判定描画
    drwa_chart2(counter_type);

  }

  
  //セルフチェックシートの描画
  function drwa_chart(chartValue){
    var ctx = document.getElementById('mycanvas');

    //前のチャートがあったら消す
    if (myChart){
        //console.log("OK");
        myChart.destroy();
    }else{
        //console.log("NG");
    }
    myChart = new Chart(ctx, {

        type: 'radar',
        data: {
            labels: ['決断力', '専門性', '自己管理', '広報力', '連携力','人間関係','患者対応','チームワーク力','総合管理','理念浸透','自己啓発','思考'],
            datasets: [{
            label: 'セルフチェックシート',
            //data: [10, 15, 11, 12, 10, 3, 4, 12,6,8,1,12],
            data: chartValue,
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
                ticks:{
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

 //タイプ判定の描画
  function drwa_chart2(chartValue){
    var ctx = document.getElementById('mycanvas2');

    //前のチャートがあったら消す
    if (myChart2){
        console.log("OK");
        myChart2.destroy();
    }else{
        console.log("NG");
    }
    myChart2 = new Chart(ctx, {

        type: 'radar',
        data: {
            labels: ['人に合わせられるタイプ', 'バランスタイプ', '感情を大切にするタイプ'],
            datasets: [{
            label: 'あなたのタイプは？',
            //data: [45, 55, 11],
            data: chartValue,
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
                ticks:{
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

 document.getElementById("save-temp").addEventListener("click", function() {
    // Xóa checkbox khỏi DOM
    var checkboxWrapper = document.getElementById("checkbox-wrapper");
    if (checkboxWrapper) {
        checkboxWrapper.remove();
    }
    // Gửi form sau khi xóa checkbox
    document.getElementById("selfcheck-form").submit();
});

document.getElementById("submit-final").addEventListener("click", function() {
    // Kiểm tra nếu checkbox không tồn tại trong DOM thì tạo lại
    var checkboxWrapper = document.getElementById("checkbox-wrapper");
    if (!checkboxWrapper) {
        var newCheckboxWrapper = document.createElement('div');
        newCheckboxWrapper.className = "checkbox";
        newCheckboxWrapper.id = "checkbox-wrapper";

        var checkboxInput = document.createElement('input');
        checkboxInput.type = "hidden";
        checkboxInput.name = "flg_finished";
        checkboxInput.value = "True";
        checkboxInput.setAttribute("aria-describedby", "id_flg_finished_helptext");
        checkboxInput.id = "id_flg_finished";

        newCheckboxWrapper.appendChild(checkboxInput);
        document.body.appendChild(newCheckboxWrapper);
    }
    // Gửi form sau khi thêm checkbox
    document.getElementById("selfcheck-form").submit();
});
