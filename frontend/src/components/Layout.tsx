import {
  SnippetsOutlined,
  HomeOutlined,
  LoginOutlined,
  UserAddOutlined
} from "@ant-design/icons";
import { Show, SignInButton, SignUpButton, UserButton } from "@clerk/react";
import {
  Button,
  Flex,
  Layout,
  Menu,
  theme,
  Tooltip,
  type MenuProps,
} from "antd";
const { Header, Content, Sider } = Layout;
import { Outlet } from "react-router";
import { useLayoutStore } from "../store/layout.store";
import { useShallow } from "zustand/react/shallow";
import { useNavigate, useLocation } from "react-router";
import React from "react";

type MenuItem = Required<MenuProps>["items"][number];

function getItem(
  label: React.ReactNode,
  key: React.Key,
  icon: React.ReactNode,
  children?: MenuItem[],
): MenuItem {
  return {
    key,
    icon,
    children,
    label,
  } as MenuItem;
}

const keyToPageMap = {
  "1": "/",
  "2": "/planner",
};

const pageToKeyMap = {
  "/": "1",
  "/planner": "2",
};

const items: MenuItem[] = [
  getItem("Home", "1", <HomeOutlined />),
  getItem("Planner", "2", <SnippetsOutlined />),
];

export default function CoreLayout() {
  let navigate = useNavigate();
  const location = useLocation();
  const { currentTab, collapsedSidebar, toggleSidebar, updateCurrentTab } =
    useLayoutStore(
      useShallow((state) => ({
        currentTab: state.currentTab,
        collapsedSidebar: state.collapsedSidebar,
        toggleSidebar: state.toggleSidebar,
        updateCurrentTab: state.updateCurrentTab,
      })),
    );

  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  React.useEffect(() => {
    updateCurrentTab(pageToKeyMap[location.pathname]);
  }, []);

  return (
    <>
      <Layout style={{ height: "100%" }}>
        <Sider
          collapsible
          collapsed={collapsedSidebar}
          onCollapse={() => toggleSidebar()}
        >
          <div className="demo-logo-vertical" />
          <Menu
            theme="dark"
            mode="inline"
            selectedKeys={currentTab ? [currentTab] : []}
            items={items}
            onClick={(info) => {
              updateCurrentTab(info.key);
              if (!collapsedSidebar) {
                toggleSidebar();
              }
              navigate(keyToPageMap[info.key]);
            }}
          />
        </Sider>
        <Layout>
          <Header style={{ padding: 0, background: colorBgContainer }}>
            <Flex style={{ float: "right", margin: "1em" }}>
              <Show when="signed-out">
                <SignInButton>
                  <Tooltip title="Sign In">
                    <Button
                      style={{ margin: "0.25em" }}
                      shape="circle"
                      icon={<LoginOutlined />}
                    ></Button>
                  </Tooltip>
                </SignInButton>
                <SignUpButton>
                  <Tooltip title="Sign Up">
                    <Button
                      style={{ margin: "0.25em" }}
                      shape="circle"
                      icon={<UserAddOutlined />}
                    >
                    </Button>
                  </Tooltip>
                </SignUpButton>
              </Show>
              <Show when="signed-in">
                <UserButton />
              </Show>
            </Flex>
          </Header>
          <Content
            style={{
              margin: "0",
              width: "100%",
              height: "100%",
              background: colorBgContainer,
              borderRadius: borderRadiusLG,
            }}
          >
            <Outlet />
          </Content>
        </Layout>
      </Layout>
    </>
  );
}
