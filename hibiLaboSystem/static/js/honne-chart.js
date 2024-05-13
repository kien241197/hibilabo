function createChart(ctx, data, label) {
  console.log("Vào đay")
  new Chart(ctx, {
    type: 'radar',
    data: {
      labels: label ? ['HP見える化', 'コンセプト・ヴィジョン', 'リーダー育成・　幹部育成', '面接・人生設計', '社内共有', '組織力', '評価制度', '個人チャート・自己分析'] : ['', '', '', '', '', '', '', ''],
      datasets: [{
        label: 'カルテット指数',
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
          max: 10,
          // 背景色
          backgroundColor: 'darkgray',
          // グリッドライン
          grid: {
          color: 'gainsboro',
          borderWidth: 4,
          },
          // アングルライン
          angleLines: {
          color: 'darkgray',
          },
          // ポイントラベル
          pointLabels: {
              color: 'black',
              backdropColor: '#ffffff',
              font: 10,

          },
      },
      },
  },
  });
}
function create_graph(id, data) {
  var strname = "mycanvas-" + id;
  var ctx = document.getElementById(strname);

  var strname1 = "mycanvas1-" + id
  var ctx1 = document.getElementById(strname1);
  console.log("a", ctx1)

  createChart(ctx, data, false)
  createChart(ctx1, data, true)
}
