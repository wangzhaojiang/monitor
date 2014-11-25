BEGIN;
CREATE TABLE `state_cpu` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `ip` varchar(30) NOT NULL,
    `time` varchar(30) NOT NULL,
    `user_use` varchar(30) NOT NULL,
    `system_use` varchar(30) NOT NULL,
    `all_use` varchar(30) NOT NULL
)
;
CREATE TABLE `state_diskio` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `ip` varchar(30) NOT NULL,
    `time` varchar(30) NOT NULL,
    `pgpgin` varchar(30) NOT NULL,
    `pgpgout` varchar(30) NOT NULL
)
;
CREATE TABLE `state_flow` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `ip` varchar(30) NOT NULL,
    `time` varchar(30) NOT NULL,
    `interface` varchar(20) NOT NULL,
    `byte` varchar(30) NOT NULL,
    `packets` varchar(30) NOT NULL
)
;
CREATE TABLE `state_memory` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `ip` varchar(30) NOT NULL,
    `time` varchar(30) NOT NULL,
    `memuse` varchar(30) NOT NULL,
    `memtotal` varchar(30) NOT NULL,
    `swaptotal` varchar(30) NOT NULL,
    `swapfree` varchar(30) NOT NULL
)
;
CREATE TABLE `state_netstat` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `ip` varchar(30) NOT NULL,
    `time` varchar(30) NOT NULL,
    `types` varchar(10) NOT NULL,
    `address` varchar(30) NOT NULL,
    `pid_programname` varchar(50) NOT NULL
)
;

COMMIT;
