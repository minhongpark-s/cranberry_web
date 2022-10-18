var ros = new ROSLIB.Ros();
 
// rosbridge websocket server와의 연결을 생성합니다.
ros.connect('ws://0.0.0.0:9090');

  ros.on('connection', function() {
    console.log('Connected to websocket server.');
    document.getElementById('header').style.backgroundColor = "#07a666";
  });

  ros.on('error', function(error) {
    console.log('Error connecting to websocket server: ', error);
  });

  ros.on('close', function() {
    console.log('Connection to websocket server closed.');
  });

  var listener = new ROSLIB.Topic({
    ros : ros,
    name : '/test/topic',
    messageType : 'std_msgs/Int16'
  });

function setBackground(context){
    var image = new Image();
    image.onload = function() {
        context.drawImage(image, 0, 0, canvas.width, canvas.height);
    }
    image.src = " image/eng1.jpg";
}

  var position = [];
  position[0]=1;
  i=1;
  // canvas 엘리먼트를 취득한다.
  const canvas = document.getElementById('myCanvas');
  // 2d모드의 그리기 객체를 취득한다. => 이 객체를 통해 canvas에 그림을 그릴 수 있다.
  const ctx = canvas.getContext("2d");

  var photoFrame = document.createElement("div");

  var image = new Image();
  image.src = "https://mblogthumb-phinf.pstatic.net/MjAyMDA1MThfNjMg/MDAxNTg5NzYxNzk5Mzk2.MqXFU237Q3JFXPvOfF45n3LpaaLKAc-3ywUzlxgQgf0g.k8rPeCURCC6Rv5gK4h_GgBFhGm30EmK8Th2-1qMa_6wg.PNG.hyerica4473/%EA%B3%B5%ED%95%99%EB%8C%80%ED%95%99_2_%EC%A0%9C1%EA%B3%B5%ED%95%99%EA%B4%80_%EC%82%AC%EB%B3%B8_2.png?type=w800";
  ctx.drawImage(image, 0, 0, 400, 300);

  listener.subscribe(function(message) {
    console.log('Received message on ' + listener.name + ': ' + message.data);
    //listener.unsubscribe(); // unsubcribe topic node.
    position[i]= message.data;

    ranNum=Math.random()*10 // 0~10

    ctx.beginPath(); // 새선 그리기 설정
    ctx.moveTo(position[i-1], position[i-1]); // 출발점 지정
    ctx.lineTo(position[i], position[i]); //도착점 지정
    ctx.stroke(); // 선 그리기
    i = i + 1;
  });