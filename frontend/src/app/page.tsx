"use client"

import { useState, useEffect } from "react"
import Navbar from "@/components/navbar";
import { Button } from "@/components/ui/button";
import { buttonVariants } from "@/components/ui/button";
import { VariantProps } from "class-variance-authority";
import { ReactNode, useRef } from "react";
import Link from "next/link";
import { cn } from "@/lib/utils";
import { motion, useScroll, useTransform, useInView } from "framer-motion";
import { ArrowRight, Github } from "lucide-react";
import Footer from "@/components/footer";

interface HeroButtonProps {
  href: string;
  text: string;
  variant?: VariantProps<typeof buttonVariants>["variant"];
  icon?: ReactNode;
  iconRight?: ReactNode;
}

interface HeroProps {
  title?: string;
  description?: string;
  mockup?: ReactNode | false;
  badge?: ReactNode | false;
  buttons?: HeroButtonProps[] | false;
  className?: string;
  bgColor?: string;
  direction?: "left" | "right";
}

function HeroCenter({ 
  title = "Give your big idea the design it deserves",
  description = "Professionally designed blocks and templates built with React, Shadcn/ui and Tailwind that will help your product stand out.",
  mockup,
  buttons,
  className 
}: HeroProps) {
  return (
    <section className={cn("relative py-20 overflow-hidden min-h-screen flex items-center", className)}>
      {/* Background Gradient - dengan dark mode support */}
      <div className="absolute inset-0 bg-gradient-to-br from-primary/5 via-transparent to-secondary/5 dark:from-primary/10 dark:via-transparent dark:to-secondary/10" />
      
      {/* Decorative blur circles - dengan dark mode support */}
      <div className="absolute top-20 left-1/4 w-64 h-64 bg-primary/10 dark:bg-primary/20 rounded-full filter blur-3xl" />
      <div className="absolute bottom-20 right-1/4 w-64 h-64 bg-secondary/10 dark:bg-secondary/20 rounded-full filter blur-3xl" />

      <div className="container mx-auto px-4 relative z-10">
        <motion.div 
          className="max-w-4xl mx-auto text-center"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          {/* Title dengan gradient yang tetap terlihat di dark mode */}
          <motion.h1 
            className="text-5xl md:text-6xl lg:text-7xl font-bold tracking-tight mb-6 bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2, duration: 0.6 }}
          >
            {title}
          </motion.h1>

          {/* Description - otomatis menyesuaikan dengan theme */}
          <motion.p 
            className="text-lg md:text-xl text-muted-foreground mb-8 max-w-2xl mx-auto"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3, duration: 0.6 }}
          >
            {description}
          </motion.p>

          {/* Buttons */}
          {buttons && buttons.length > 0 && (
            <motion.div 
              className="flex flex-col sm:flex-row gap-4 justify-center mb-16"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4, duration: 0.6 }}
            >
              {buttons.map((button, index) => (
                <motion.div
                  key={index}
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  <Link
                    href={button.href}
                    className={cn(
                      buttonVariants({ 
                        variant: button.variant || "default",
                        size: "lg" 
                      }),
                      "gap-2 text-base px-8"
                    )}
                  >
                    {button.icon}
                    {button.text}
                    {button.iconRight}
                  </Link>
                </motion.div>
              ))}
            </motion.div>
          )}

          {/* Mockup / Dashboard Preview - dengan dark mode support */}
          {mockup && (
            <motion.div 
              className="relative mt-8"
              initial={{ opacity: 0, y: 40 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.5, duration: 0.8 }}
            >
              <motion.div
                animate={{ 
                  y: [0, -5, 0],
                }}
                transition={{ 
                  duration: 4,
                  repeat: Infinity,
                  ease: "easeInOut"
                }}
              >
                {mockup}
              </motion.div>
              
              {/* Decorative elements dengan dark mode support */}
              <div className="absolute -top-4 -left-4 w-24 h-24 bg-primary/20 dark:bg-primary/30 rounded-full filter blur-2xl" />
              <div className="absolute -bottom-4 -right-4 w-24 h-24 bg-secondary/20 dark:bg-secondary/30 rounded-full filter blur-2xl" />
            </motion.div>
          )}
        </motion.div>
      </div>
    </section>
  );
}

function ScrollHero({ 
  title, 
  description, 
  mockup, 
  badge, 
  buttons, 
  className,
  bgColor = "from-primary/5 via-transparent to-secondary/5",
  direction = "left"
}: HeroProps) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: false, amount: 0.3 });
  
  // Parallax effect
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"]
  });
  
  const y = useTransform(scrollYProgress, [0, 1], [100, -100]);
  const opacity = useTransform(scrollYProgress, [0, 0.3, 0.6, 1], [0, 1, 1, 0]);
  const scale = useTransform(scrollYProgress, [0, 0.5, 1], [0.8, 1, 0.8]);
  const rotate = useTransform(scrollYProgress, [0, 1], [direction === "left" ? -10 : 10, direction === "left" ? 10 : -10]);
  const x = useTransform(scrollYProgress, [0, 0.5, 1], [direction === "left" ? -100 : 100, 0, direction === "left" ? 100 : -100]);

  // Konversi bgColor untuk dark mode
  const darkBgColor = bgColor.replace(/\/5|\/10/g, '/20');

  return (
    <motion.section 
      ref={ref}
      style={{ opacity }}
      className={cn("relative py-20 overflow-hidden min-h-screen flex items-center", className)}
    >
      {/* Background dengan efek parallax - dengan dark mode support */}
      <motion.div 
        style={{ y, scale }}
        className={`absolute inset-0 bg-gradient-to-br ${bgColor} dark:${darkBgColor}`}
      />
      
      {/* Animated elements dengan efek berbeda per section - dengan dark mode support */}
      <motion.div
        style={{ rotate }}
        className="absolute top-20 left-20 w-64 h-64 bg-primary/10 dark:bg-primary/20 rounded-full filter blur-3xl"
      />
      <motion.div
        style={{ rotate: useTransform(scrollYProgress, [0, 1], [0, 360]) }}
        className="absolute bottom-20 right-20 w-64 h-64 bg-secondary/10 dark:bg-secondary/20 rounded-full filter blur-3xl"
      />

      <div className="container mx-auto px-4 relative z-10">
        <motion.div 
          className={`flex flex-col lg:flex-row items-center gap-12 ${direction === "right" ? "lg:flex-row-reverse" : ""}`}
        >
          {/* Content dengan efek berbeda */}
          <motion.div 
            className="flex-1 text-center lg:text-left"
            initial={{ opacity: 0, x: direction === "left" ? -50 : 50 }}
            animate={isInView ? { opacity: 1, x: 0 } : {}}
            transition={{ duration: 0.8 }}
          >
            {badge && (
              <motion.div 
                className="inline-block mb-6"
                initial={{ opacity: 0, y: -20 }}
                animate={isInView ? { opacity: 1, y: 0 } : {}}
                transition={{ delay: 0.2 }}
              >
                {badge}
              </motion.div>
            )}

            <motion.h1 
              className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight mb-6"
              initial={{ opacity: 0, y: 30 }}
              animate={isInView ? { opacity: 1, y: 0 } : {}}
              transition={{ delay: 0.3 }}
            >
              {title}
            </motion.h1>

            <motion.p 
              className="text-lg md:text-xl text-muted-foreground mb-8 max-w-2xl mx-auto lg:mx-0"
              initial={{ opacity: 0, y: 30 }}
              animate={isInView ? { opacity: 1, y: 0 } : {}}
              transition={{ delay: 0.4 }}
            >
              {description}
            </motion.p>

            {buttons && buttons.length > 0 && (
              <motion.div 
                className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start"
                initial={{ opacity: 0, y: 30 }}
                animate={isInView ? { opacity: 1, y: 0 } : {}}
                transition={{ delay: 0.5 }}
              >
                {buttons.map((button, index) => (
                  <motion.div
                    key={index}
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                  >
                    <Link
                      href={button.href}
                      className={cn(
                        buttonVariants({ 
                          variant: button.variant || "default",
                          size: "lg" 
                        }),
                        "group inline-flex items-center gap-2"
                      )}
                    >
                      {button.icon}
                      {button.text}
                      {button.iconRight}
                    </Link>
                  </motion.div>
                ))}
              </motion.div>
            )}
          </motion.div>

          {/* Mockup dengan efek berbeda */}
          {mockup && (
            <motion.div 
              className="flex-1 w-full"
              style={{ x }}
              initial={{ opacity: 0, scale: 0.8 }}
              animate={isInView ? { opacity: 1, scale: 1 } : {}}
              transition={{ duration: 0.8, delay: 0.3 }}
            >
              <motion.div
                animate={isInView ? {
                  y: [0, -10, 0],
                  rotate: [0, direction === "left" ? 2 : -2, 0]
                } : {}}
                transition={{
                  duration: 4,
                  repeat: Infinity,
                  ease: "easeInOut"
                }}
              >
                {mockup}
              </motion.div>
            </motion.div>
          )}
        </motion.div>
      </div>
    </motion.section>
  );
}

export default function Home() {
  return (
    <>
      <Navbar/>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
      >
        {/* Hero 1: Center Layout (seperti gambar) */}
        <HeroCenter
          title="Give your big idea the design it deserves"
          description="Professionally designed blocks and templates built with React, Shadcn/ui and Tailwind that will help your product stand out."
          buttons={[
            {
              href: "/get-started",
              text: "Get Started",
              variant: "default",
              iconRight: <ArrowRight className="h-4 w-4" />
            },
            {
              href: "https://github.com",
              text: "GitHub",
              variant: "outline",
              icon: <Github className="h-4 w-4" />
            }
          ]}
          mockup={
            <div className="bg-background/80 backdrop-blur-sm border rounded-2xl shadow-2xl dark:shadow-primary/10 p-6">
              {/* Dashboard Mockup */}
              <div className="space-y-6">
                {/* Header */}
                <div className="flex items-center justify-between border-b dark:border-gray-800 pb-4">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 bg-primary/20 dark:bg-primary/30 rounded-lg" />
                    <span className="font-semibold">Acme Inc.</span>
                  </div>
                  <div className="flex items-center gap-4 text-sm text-muted-foreground">
                    <span>Quick Create</span>
                    <span>Dashboard</span>
                    <span>Lifecycle</span>
                  </div>
                </div>

                {/* Content */}
                <div className="grid grid-cols-2 gap-4">
                  {/* Left column - Documents */}
                  <div className="space-y-2">
                    <p className="text-sm font-medium text-muted-foreground">Documents</p>
                    <div className="space-y-1">
                      <div className="text-sm">Total Revenue: <span className="text-green-500">+12.5%</span></div>
                      <div className="text-sm">New Customers: <span className="text-green-500">+30%</span></div>
                      <div className="text-sm">Active Accounts: <span className="text-green-500">+22.5%</span></div>
                      <div className="text-sm">Growth Rate: <span className="text-green-500">+4.5%</span></div>
                    </div>
                  </div>

                  {/* Right column - Stats */}
                  <div className="space-y-2">
                    <div className="grid grid-cols-2 gap-2">
                      <div className="bg-muted/50 dark:bg-gray-800/50 rounded-lg p-3">
                        <div className="text-xs text-muted-foreground">Revenue</div>
                        <div className="text-lg font-semibold">$1,250.00</div>
                      </div>
                      <div className="bg-muted/50 dark:bg-gray-800/50 rounded-lg p-3">
                        <div className="text-xs text-muted-foreground">Customers</div>
                        <div className="text-lg font-semibold">1,234</div>
                      </div>
                      <div className="bg-muted/50 dark:bg-gray-800/50 rounded-lg p-3">
                        <div className="text-xs text-muted-foreground">Accounts</div>
                        <div className="text-lg font-semibold">45,678</div>
                      </div>
                      <div className="bg-muted/50 dark:bg-gray-800/50 rounded-lg p-3">
                        <div className="text-xs text-muted-foreground">Growth</div>
                        <div className="text-lg font-semibold">4.5%</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          }
        />

        {/* Hero 2: Parallax Scroll Effect dengan background biru */}
        <ScrollHero
          title="Fitur Unggulan untuk Kesuksesanmu"
          description="Dapatkan akses ke ribuan materi pembelajaran, quiz interaktif, dan sertifikat resmi."
          bgColor="from-blue-500/10 via-transparent to-purple-500/10"
          direction="right"
          badge={<span className="bg-blue-500/10 text-blue-500 px-4 py-2 rounded-full text-sm">🚀 Fitur Premium</span>}
          buttons={[
            { href: "/features", text: "Jelajahi Fitur", variant: "default", icon: <span>✨</span> },
            { href: "/pricing", text: "Lihat Harga", variant: "outline" }
          ]}
          mockup={
            <div className="bg-gradient-to-br from-blue-500 to-purple-500 p-1 rounded-3xl shadow-2xl">
              <div className="bg-background rounded-3xl p-6">
                <div className="grid grid-cols-2 gap-4">
                  <div className="p-3 bg-blue-50 rounded-xl">
                    <div className="text-2xl mb-2">📚</div>
                    <div className="font-semibold">1000+</div>
                    <div className="text-xs text-muted-foreground">Materi</div>
                  </div>
                  <div className="p-3 bg-purple-50 rounded-xl">
                    <div className="text-2xl mb-2">🎯</div>
                    <div className="font-semibold">50+</div>
                    <div className="text-xs text-muted-foreground">Kursus</div>
                  </div>
                </div>
              </div>
            </div>
          }
        />

        {/* Hero 3: Scale & Rotate Effect dengan background hijau */}
        <ScrollHero
          title="Belajar dari Mentor Berpengalaman"
          description="Dibimbing langsung oleh praktisi industri dengan pengalaman bertahun-tahun di bidangnya."
          bgColor="from-green-500/10 via-transparent to-emerald-500/10"
          direction="left"
          badge={<span className="bg-green-500/10 text-green-500 px-4 py-2 rounded-full text-sm">👨‍🏫 Mentor Expert</span>}
          buttons={[
            { href: "/mentors", text: "Lihat Mentor", variant: "default", icon: <span>👥</span> },
            { href: "/testimonials", text: "Testimoni", variant: "outline" }
          ]}
          mockup={
            <div className="bg-gradient-to-br from-green-500 to-emerald-500 p-1 rounded-3xl shadow-2xl">
              <div className="bg-background rounded-3xl p-4">
                <div className="flex items-center gap-3">
                  <div className="w-16 h-16 bg-green-500/20 rounded-full flex items-center justify-center text-3xl">👤</div>
                  <div>
                    <h3 className="font-semibold">John Doe</h3>
                    <p className="text-sm text-muted-foreground">Senior Developer</p>
                    <div className="flex gap-1 mt-1">⭐⭐⭐⭐⭐</div>
                  </div>
                </div>
              </div>
            </div>
          }
        />

        {/* Hero 4: Slide & Flip Effect dengan background orange */}
        <ScrollHero
          title="Dapatkan Sertifikat Resmi"
          description="Setiap kursus dilengkapi dengan sertifikat resmi yang bisa kamu gunakan untuk karirmu."
          bgColor="from-orange-500/10 via-transparent to-red-500/10"
          direction="right"
          badge={<span className="bg-orange-500/10 text-orange-500 px-4 py-2 rounded-full text-sm">📜 Sertifikat</span>}
          buttons={[
            { href: "/certificates", text: "Lihat Sertifikat", variant: "default", icon: <span>🏆</span> },
            { href: "/gallery", text: "Galeri", variant: "outline" }
          ]}
          mockup={
            <div className="bg-gradient-to-br from-orange-500 to-red-500 p-1 rounded-3xl shadow-2xl">
              <div className="bg-background rounded-3xl p-6">
                <div className="border-2 border-orange-500/20 rounded-xl p-4 text-center">
                  <div className="text-4xl mb-2">📜</div>
                  <h3 className="font-semibold">Certificate of Completion</h3>
                  <p className="text-xs text-muted-foreground mt-2">Web Development</p>
                  <div className="mt-3 text-xs text-orange-500">+1500 alumni</div>
                </div>
              </div>
            </div>
          }
        />
      </motion.div>

      {/* Scroll Indicator */}
      <motion.div 
        className="fixed bottom-8 left-1/2 transform -translate-x-1/2 z-50"
        animate={{ y: [0, 10, 0] }}
        transition={{ duration: 2, repeat: Infinity }}
      >
        {/* <div className="bg-background/80 backdrop-blur-sm px-4 py-2 rounded-full shadow-lg text-sm">
          ⬇️ Scroll untuk lihat lebih banyak
        </div> */}
      </motion.div>
      <Footer/>
    </>
  )
}