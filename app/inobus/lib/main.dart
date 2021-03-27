import 'package:flutter/material.dart';

import 'frame/home.dart';
import 'frame/introduce.dart';

void main() {
  runApp(InobusApp());
}

class InobusApp extends StatefulWidget {
  @override
  _InobusApp createState() => _InobusApp();
}

class _InobusApp extends State<InobusApp> {
  bool checking = false;
  Color representativeColor = Color(0xffF04C18);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'INOBUS application',
        home: checking
            ? HomeFrame(
                title: 'INOBUS',
                backgroundColor: representativeColor,
                pointColor: Colors.white,
              )
            : IntroduceFrame(
                onPressButton: () {
                  setState(() {
                    checking = true;
                  });
                },
              ),
        theme: ThemeData(
          // 테마 색상 설정
          accentColor: representativeColor,
        ));
  }
}
