import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:mobile/models/user_model.dart';
import '../providers/auth_provider.dart';
import '../utils/validator.dart';
import '../widgets/custom_text_field.dart';
import '../widgets/loading_button.dart';
import 'register_screen.dart';
import 'home_screen.dart';

class LoginScreen extends ConsumerStatefulWidget {
  const LoginScreen({super.key});

  @override
  ConsumerState<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends ConsumerState<LoginScreen> {
  final _formKey = GlobalKey<FormState>();

  @override
  void initState() {
    super.initState();
    // Reset form saat screen dibuka
    WidgetsBinding.instance.addPostFrameCallback((_) {
      ref.read(emailProvider.notifier).state = '';
      ref.read(passwordProvider.notifier).state = '';
      ref.read(errorMessageProvider.notifier).state = null;
    });
  }

  @override
  Widget build(BuildContext context) {
    final authStatus = ref.watch(authStatusProvider);
    final errorMessage = ref.watch(errorMessageProvider);
    final email = ref.watch(emailProvider);
    final password = ref.watch(passwordProvider);
    final isPasswordVisible = ref.watch(isPasswordVisibleProvider);
    
    final authService = ref.read(authProvider);

    // Auto redirect jika sudah login
    ref.listen<AuthStatus>(authStatusProvider, (previous, next) {
      if (next == AuthStatus.authenticated) {
        Navigator.of(context).pushReplacement(
          MaterialPageRoute(builder: (_) => const HomeScreen()),
        );
      }
    });

    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24.0),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SizedBox(height: 40),
                
                // Header
                Center(
                  child: Column(
                    children: [
                      Container(
                        width: 80,
                        height: 80,
                        decoration: BoxDecoration(
                          color: Theme.of(context).primaryColor.withOpacity(0.1),
                          shape: BoxShape.circle,
                        ),
                        child: Icon(
                          Icons.school,
                          size: 40,
                          color: Theme.of(context).primaryColor,
                        ),
                      ),
                      const SizedBox(height: 24),
                      Text(
                        'Selamat Datang Kembali',
                        style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 8),
                      Text(
                        'Silakan login untuk melanjutkan',
                        style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                          color: Colors.grey.shade600,
                        ),
                      ),
                    ],
                  ),
                ),
                
                const SizedBox(height: 40),

                // Error Message
                if (errorMessage != null) ...[
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: Colors.red.shade50,
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: Colors.red.shade200),
                    ),
                    child: Row(
                      children: [
                        Icon(Icons.error_outline, color: Colors.red.shade700),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Text(
                            errorMessage,
                            style: TextStyle(color: Colors.red.shade700),
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 24),
                ],

                // Email Field
                CustomTextField(
                  label: 'Email',
                  hint: 'Masukkan email Anda',
                  prefixIcon: Icons.email_outlined,
                  provider: emailProvider,
                  validator: Validators.validateEmail,
                  keyboardType: TextInputType.emailAddress,
                ),
                
                const SizedBox(height: 16),

                // Password Field
                CustomTextField(
                  label: 'Password',
                  hint: 'Masukkan password Anda',
                  prefixIcon: Icons.lock_outline,
                  obscureText: !isPasswordVisible,
                  provider: passwordProvider,
                  validator: Validators.validatePassword,
                  suffixIcon: IconButton(
                    icon: Icon(
                      isPasswordVisible ? Icons.visibility_off : Icons.visibility,
                    ),
                    onPressed: () {
                      ref.read(isPasswordVisibleProvider.notifier).state = 
                          !isPasswordVisible;
                    },
                  ),
                ),

                const SizedBox(height: 12),

                // Forgot Password
                Align(
                  alignment: Alignment.centerRight,
                  child: TextButton(
                    onPressed: () {
                      // TODO: Implement forgot password
                    },
                    child: const Text('Lupa Password?'),
                  ),
                ),

                const SizedBox(height: 24),

                // Login Button
                LoadingButton(
                  isLoading: authStatus == AuthStatus.loading,
                  onPressed: () {
                    if (_formKey.currentState!.validate()) {
                      authService.login(email, password);
                    }
                  },
                  text: 'Login',
                ),

                const SizedBox(height: 16),

                // Register Link
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text(
                      'Belum punya akun? ',
                      style: TextStyle(color: Colors.grey.shade600),
                    ),
                    TextButton(
                      onPressed: () {
                        Navigator.of(context).push(
                          MaterialPageRoute(
                            builder: (_) => const RegisterScreen(),
                          ),
                        );
                      },
                      child: const Text(
                        'Daftar Sekarang',
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}