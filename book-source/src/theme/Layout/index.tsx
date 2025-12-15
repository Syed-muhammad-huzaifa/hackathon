import React from "react";
import OriginalLayout from "@theme-original/Layout";
import type { Props } from "@theme/Layout";
import { ChatWidget } from "@site/src/components/ChatWidget";

export default function Layout(props: Props): JSX.Element {
  return (
    <>
      <OriginalLayout {...props} />
      <ChatWidget />
    </>
  );
}
