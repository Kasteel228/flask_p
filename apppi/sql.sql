create table if not exists mainmenu (
id integer primary key autoincrement,
title text not null,
irl text not null
);

create table if not exists death (
id integer primary key autoincrement,
title text not null,
death text not null,
url text not null
);