// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract Kenesis_Logger_v1 {
  struct Task {
    string employee_name;
    string employer_name;
    string task_name;
    string task_detials;
    string date_time;
  }
  mapping (address => Task) list_task;
  constructor() {
  }


}
