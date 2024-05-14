function chart(ctx, data, labels){

  new Chart(ctx, {
    type: 'radar',
    data: {
      labels: labels ? ['決断力', '専門性', '自己管理', '広報力', '連携力','人間関係','患者対応','チームワーク力','総合管理','理念浸透','自己啓発','思考'] : ['', '', '', '', '','', '', '', '','', '', ''],
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

function create_chart(id, data) {
    var strname = "mycanvas-" + id;
    var strname1 = "mycanvas1-" + id;

    //図を動的に生成
    var ctx = document.getElementById(strname);
    var ctx1 = document.getElementById(strname1);

    chart(ctx, data, false)
    chart(ctx1, data, true)


}