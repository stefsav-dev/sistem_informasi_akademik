import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_riverpod/legacy.dart';
import 'package:introduction_screen/introduction_screen.dart';


final hasSeenIntroductionProvider = StateProvider<bool>((ref) => false);

final introductionPageProvider = StateProvider<int>((ref) => 0);

final introductionItemsProvider = Provider<List<PageViewModel>>((ref) {
  return [
    PageViewModel(
      title: "Selamat Datang",
      body: "Temukan fitur-fitur menarik dalam aplikasi kami",
      image: Center(
        child: Icon(
          Icons.rocket_launch,
          size: 150,
          color: Colors.blue,
        ),
      ),
      decoration: const PageDecoration(
        titleTextStyle: TextStyle(
          fontSize: 28,
          fontWeight: FontWeight.bold,
        ),
        bodyTextStyle: TextStyle(
          fontSize: 16,
        ),
        imagePadding: EdgeInsets.only(top: 40),
      ),
    ),
    PageViewModel(
      title: "Mudah Digunakan",
      body: "Antarmuka yang sederhana dan intuitif",
      image: Center(
        child: Icon(
          Icons.thumb_up,
          size: 150,
          color: Colors.green,
        ),
      ),
      decoration: const PageDecoration(
        titleTextStyle: TextStyle(
          fontSize: 28,
          fontWeight: FontWeight.bold,
        ),
        bodyTextStyle: TextStyle(
          fontSize: 16,
        ),
        imagePadding: EdgeInsets.only(top: 40),
      ),
    ),
    PageViewModel(
      title: "Siap Memulai?",
      body: "Ayo mulai petualangan Anda bersama kami!",
      image: Center(
        child: Icon(
          Icons.start,
          size: 150,
          color: Colors.orange,
        ),
      ),
      decoration: const PageDecoration(
        titleTextStyle: TextStyle(
          fontSize: 28,
          fontWeight: FontWeight.bold,
        ),
        bodyTextStyle: TextStyle(
          fontSize: 16,
        ),
        imagePadding: EdgeInsets.only(top: 40),
      ),
    ),
  ];
});