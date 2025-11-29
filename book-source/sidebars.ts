import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    'preface',
    {
      type: 'category',
      label: 'Chapter 1: Introduction to Physical AI',
      items: [
        'chapter1/section1-physical-ai',
        'chapter1/section2-digital-vs-physical-ai',
        'chapter1/section3-ai-in-bodies',
        'chapter1/section4-real-world-constraints',
      ],
    },
    {
      type: 'category',
      label: 'Part 2: The Robotic Nervous System (ROS 2)',
      items: [
        'part2-ros/chapter1-ros-architecture',
        'part2-ros/chapter2-python-ros2-packages',
        'part2-ros/chapter3-urdf',
      ],
    },
    {
      type: 'category',
      label: 'Part 3: The Digital Twin (Gazebo & Unity)',
      items: [
        'part3-digital-twin/chapter1-physics-simulation',
      ],
    },  ],

  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    'intro',
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
   */
};

export default sidebars;
