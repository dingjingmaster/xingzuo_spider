-- 星座表
CREATE TABLE IF NOT EXISTS `article`
(
    `id`         INT(11) PRIMARY KEY AUTO_INCREMENT, -- id 自增
    `title`      VARCHAR(150)                 DEFAULT NULL,
    `time`       datetime,
    `pageviews`  INT(11),
    `author`     VARCHAR(150)                 DEFAULT NULL,
    `textTop`    text                NOT NULL,
    `img`        VARCHAR(300)        NOT NULL,
    `textbottom` text                NOT NULL,       -- 类型
    `type`       int(11),
    `url`        VARCHAR(300) UNIQUE NOT NULL DEFAULT '',
) ENGINE = MyISAM
  DEFAULT CHARSET = utf8;