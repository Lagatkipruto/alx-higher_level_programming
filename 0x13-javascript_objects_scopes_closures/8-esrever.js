#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (a, current) {
    a.push(current);
    return a;
  }, []);
};
