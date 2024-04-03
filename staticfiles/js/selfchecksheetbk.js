//ABCとタイプ集計
function func_count1(){

    //左右テーブルと結果格納テーブルの獲得
    var mytable = document.getElementById("selftchek_table");
    var mytable2 = document.getElementById("selftchek_table2");
    var resulttable = document.getElementById("calc_resul");
    var circl = document.getElementById("circl");
    var square = document.getElementById("square");
    var traiangle = document.getElementById("traiangle");
    var index1 = document.getElementById("index1");
    var index2 = document.getElementById("index2");
    var index3 = document.getElementById("index3");
    var index4 = document.getElementById("index4");
    var index5 = document.getElementById("index5");
    var index6 = document.getElementById("index6");
    var index7 = document.getElementById("index7");
    var index8 = document.getElementById("index8");
    var index9 = document.getElementById("index9");
    var index10 = document.getElementById("index10");
    var index11 = document.getElementById("index11");
    var index12 = document.getElementById("index12");



    //分類ごとの集計の器クリア
    var counter_group = new Array(12);
    for ( var i=0; i <= 12; i++){
        counter_group[i]=0;
    }
    //分類集計の添え字カウンタクリア
    var idx_group = 0;

    //タイプ別の集計の器クリア
    var counter_type = new Array(3);
    for ( var i=0; i <= 3; i++){
        counter_type[i]=0;
    }

    //引き渡し用のid分の器クリア
    var index_answer = new Array(60);
    for ( var i=0; i <= 60; i++){
        index_answer[i]=0;
    }


    // name名「option_result1」を全てを取得
    let elm = document.getElementsByName("option_result1");

    // name名「option_result1」のテキスト（slectの選択状態）を集計する
    for (let i = 0; i < elm.length; i++) {    
        //console.log (i + "行:" + elm[i].value);

        //ポイントを分類毎に累計していく
        counter_group[idx_group] += Number(elm[i].value);
        //分類は5質問毎に変わるため剰余を求め、分類が切り替わったら分類集計の添え字カウンタをアップ
        var remain = i % 5;
        if (remain == 4) {
            idx_group ++;
        }        

        //ポイントが発生している時にはタイプ別の集計を行う
        if (Number(elm[i].value) > 0){
            //iが0～29までは左のテーブル、30～59までが右のテーブル
            var strtype = "";
            if (i < 30) {
                strtype = mytable.rows[i + 1].cells[4].innerText;
            }
            else{
                strtype = mytable2.rows[i - 29].cells[4].innerText;            
            }

            //タイプ別にカウント
            switch (strtype) {
                    case 'circle':
                        counter_type[0] += Number(elm[i].value);
                        //console.log (i + "行:〇")
                        break;
                    case 'square':
                        counter_type[1] += Number(elm[i].value);
                        //console.log (i + "行:□")
                        break;                    
                    case 'triangle':
                        counter_type[2] += Number(elm[i].value);
                        //console.log (i + "行:△")
                        break;                    
                    default:
                        console.log (i + "行:" + strtype);
                        break;
            } 
            index_answer[i] = Number(elm[i].value)
        }

    }


    //回答をセット
    var strname = '';
    var strindex = '';
    var target = '';
    for (let i = 0; i < 60; i++) {
        strindex = i + 1;
        strname = 'a' + strindex;
        target = document.getElementById(strname);
        target.value = index_answer[i];
    }



    //集計したものを1類～12類の結果セット
    for (let i = 0; i < 12; i++) {
        resulttable.rows[1].cells[i].innerText = counter_group[i];
    }
    index1.value  = counter_group[0];
    index2.value  = counter_group[1];
    index3.value  = counter_group[2];
    index4.value  = counter_group[3];
    index5.value  = counter_group[4];
    index6.value  = counter_group[5];
    index7.value  = counter_group[6];
    index8.value  = counter_group[7];
    index9.value  = counter_group[8];
    index10.value  = counter_group[9];
    index11.value  = counter_group[10];
    index12.value  = counter_group[11];

    //まる（人合わせ)、しかく（バランス)、さんかく(感情)の順にセット
    resulttable.rows[1].cells[12].innerText = counter_type[0];
    circl.value = counter_type[0];
    resulttable.rows[1].cells[13].innerText = counter_type[1];
    square.value = counter_type[1];
    resulttable.rows[1].cells[14].innerText = counter_type[2];
    traiangle.value = counter_type[2];

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
            data: [chartValue[0], chartValue[1], chartValue[2], chartValue[3], chartValue[4], chartValue[5], chartValue[6], chartValue[7], chartValue[8], chartValue[9], chartValue[10], chartValue[11]],
            // データライン
            borderColor: 'blue',
            borderWidth: 2,
            }],
        },
        options: {
            scales: {
            r: {
                // 最小値・最大値
                min: 0,
                max: 15,
                // 背景色
                backgroundColor: 'lightyellow',
                // グリッドライン
                grid: {
                color: 'white',
                },
                // アングルライン
                angleLines: {
                color: 'black',
                },
                // ポイントラベル
                pointLabels: {
                color: 'blue',
                backdropColor: '#ddf',
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
            data: [chartValue[0], chartValue[1], chartValue[2]],
            // データライン
            borderColor: 'green',
            borderWidth: 2,
            }],
        },
        options: {
            scales: {
            r: {
                // 最小値・最大値
                min: 0,
                max: 60,
                // 背景色
                backgroundColor: 'lightyellow',
                // グリッドライン
                grid: {
                color: 'lightyellow',
                },
                // アングルライン
                angleLines: {
                color: 'black',
                },
                // ポイントラベル
                pointLabels: {
                color: 'blue',
                backdropColor: '#ddf',
                backdropPadding: 5,
                padding: 20,
                },
            },
            },
        },
    });
 }
