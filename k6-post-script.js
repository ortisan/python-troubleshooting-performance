import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '10s', target: 10, rps: 1 },
    { duration: '10s', target: 10, rps: 1 },
    { duration: '10s', target: 20, rps: 1 },
    { duration: '1h', target: 20, rps: 1 },
  ],
};

export default function () {

  const payload = JSON.stringify({
    epoch_timestamp: 123456,
    symbol: 'ETH',
    value: 10.0,
  });

  var params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  let res = http.post("http://localhost:8000/tick/", payload, params);
  // console.log(JSON.stringify(res))
  check(res, { 'status was 200': (r) => r.status == 201 });
  sleep(1);
}