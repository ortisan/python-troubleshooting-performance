import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '10s', target: 10, rps: 1 },
    { duration: '10s', target: 10, rps: 1 },
    { duration: '10s', target: 20, rps: 1 },
    { duration: '10m', target: 20, rps: 1 },
  ],
};

export default function () {

  var params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  let res = http.get("http://localhost:8000", params);
  check(res, { 'status was 200': (r) => r.status == 200 });
  sleep(1);
}