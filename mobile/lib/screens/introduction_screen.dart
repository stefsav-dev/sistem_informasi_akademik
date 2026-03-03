import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:introduction_screen/introduction_screen.dart' as intro;
import '../providers/introduction_provider.dart';

class IntroductionScreen extends ConsumerWidget {
  const IntroductionScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final pages = ref.watch(introductionItemsProvider);
    final pageIndex = ref.watch(introductionPageProvider);

    return intro.IntroductionScreen(
      pages: pages,
      initialPage: pageIndex,
      onDone: () {
        // Tandai bahwa user sudah melihat introduction
        ref.read(hasSeenIntroductionProvider.notifier).state = true;
      },
      onSkip: () {
        // Tandai bahwa user sudah melewati introduction
        ref.read(hasSeenIntroductionProvider.notifier).state = true;
      },
      showSkipButton: true,
      skip: const Text(
        'Skip',
        style: TextStyle(fontSize: 16),
      ),
      next: const Icon(Icons.arrow_forward),
      done: const Text(
        'Get Started',
        style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
      ),
      curve: Curves.easeInOut,
      controlsMargin: const EdgeInsets.all(16),
      dotsDecorator: intro.DotsDecorator(
        size: const Size.square(8),
        activeSize: const Size(24, 8),
        activeShape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(4),
        ),
        activeColor: Colors.blue,
      ),
      globalBackgroundColor: Colors.white,
      onChange: (index) {
        ref.read(introductionPageProvider.notifier).state = index;
      },
    );
  }
}
